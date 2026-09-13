"""Execute the documented commands against disposable repositories, without a model or network."""

import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def documented_command(skill, name):
    text = (ROOT / "skills" / skill / "SKILL.md").read_text()
    match = re.search(rf"<!-- test:{re.escape(name)} -->\s*```bash\n(.*?)\n```", text, re.S)
    if not match:
        raise AssertionError(f"Missing executable example: {name}")
    return match.group(1)


def run(cwd, *args, check=True, env=None):
    env = {**(os.environ if env is None else env),
           "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull}
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=check, env=env)


class GuidanceDiscoveryTest(unittest.TestCase):
    def setUp(self):
        if not shutil.which("rg"):
            self.skipTest("ripgrep is required for the documented discovery commands")
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        run(self.root, "git", "init", "-q")

    def touch(self, name, text="fixture\n"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def discover(self, name):
        env = {**os.environ, "RIPGREP_CONFIG_PATH": ""}
        result = run(self.root, "bash", "-c", documented_command("setup-agent-project", name),
                     check=False, env=env)
        self.assertIn(result.returncode, (0, 1), result.stderr)
        return set(result.stdout.splitlines())

    def test_hidden_nested_and_client_guidance_is_found_without_unrelated_files(self):
        expected = {
            "AGENTS.md", "AGENTS.override.md", "CLAUDE.md", "CLAUDE.local.md", ".gitmodules",
            ".agents/skills/example/SKILL.md", ".agent-memory/project.md",
            ".claude/rules/project.md", ".codex/config.toml", "docs/guide.md", "learning/topic.md",
            "packages/api/AGENTS.override.md", "packages/api/CLAUDE.md",
            "packages/api/.claude/rules/api.md", "packages/api/.agents/skills/api/SKILL.md",
        }
        excluded = {
            ".env", ".private/secret", "src/main.py", "node_modules/pkg/AGENTS.md",
            ".venv/lib/CLAUDE.md", ".git/AGENTS.md", "vendor/repo/.git/CLAUDE.md",
        }
        for name in expected | excluded:
            self.touch(name)
        self.assertEqual(self.discover("guidance-discovery"), expected)

    def test_ignored_target_is_found_only_by_scoped_second_pass(self):
        self.touch(".gitignore", ".claude/\n.private/\n")
        self.touch(".claude/skills/local/SKILL.md")
        self.touch(".claude/.git/AGENTS.md")
        self.touch(".private/CLAUDE.md")
        self.assertEqual(self.discover("guidance-discovery"), set())
        self.assertEqual(self.discover("ignored-guidance-discovery"),
                         {".claude/skills/local/SKILL.md"})

    def test_empty_inventory_is_not_a_command_error(self):
        self.assertEqual(self.discover("guidance-discovery"), set())


class RemoteCleanupTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.remote = self.root / "remote.git"
        self.repo = self.root / "checkout"
        run(self.root, "git", "init", "-q", "--bare", str(self.remote))
        run(self.root, "git", "init", "-q", "-b", "master", str(self.repo))
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.a = self.commit("A")
        self.git("branch", "main")
        self.git("remote", "add", "release", str(self.remote))
        self.git("push", "release", "master", "main")
        self.remote_git("symbolic-ref", "HEAD", "refs/heads/main")

    def git(self, *args, check=True):
        return run(self.repo, "git", *args, check=check)

    def remote_git(self, *args):
        return run(self.root, "git", f"--git-dir={self.remote}", *args)

    def commit(self, message):
        self.git("commit", "-q", "--allow-empty", "-m", message)
        return self.git("rev-parse", "HEAD").stdout.strip()

    def cleanup(self):
        return run(self.repo, "bash", "-c", documented_command("rename-master-to-main", "remote-cleanup"),
                   check=False, env={**os.environ, "migration_remote": "release"})

    def tip(self, branch):
        return self.remote_git("rev-parse", f"refs/heads/{branch}").stdout.strip()

    def test_stale_local_branch_cannot_delete_ahead_remote_master(self):
        b = self.commit("B only on remote master")
        self.git("push", "release", "master")
        self.git("switch", "main")
        self.git("branch", "-f", "master", self.a)
        result = self.cleanup()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.tip("master"), b)
        self.assertEqual(self.tip("main"), self.a)

    def test_divergent_remote_main_cannot_delete_master(self):
        b = self.commit("B")
        self.git("push", "release", "master")
        self.git("switch", "main")
        c = self.commit("C")
        self.git("push", "release", "main")
        self.assertNotEqual(self.cleanup().returncode, 0)
        self.assertEqual(self.tip("master"), b)
        self.assertEqual(self.tip("main"), c)

    def test_contained_history_is_deleted_on_selected_non_origin_remote(self):
        decoy = self.root / "origin.git"
        run(self.root, "git", "clone", "-q", "--bare", str(self.remote), str(decoy))
        self.git("remote", "add", "origin", str(decoy))
        self.git("switch", "main")
        b = self.commit("B on main")
        self.git("push", "release", "main")
        result = self.cleanup()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.remote_git("for-each-ref", "refs/heads/master").stdout, "")
        self.assertEqual(self.tip("main"), b)
        self.assertEqual(run(self.root, "git", f"--git-dir={decoy}", "rev-parse",
                             "refs/heads/master").stdout.strip(), self.a)

    def test_master_change_during_push_is_rejected_by_exact_lease(self):
        b = self.commit("Concurrent B")
        # Copy the object to the remote without advancing master until the pre-push hook.
        self.git("push", "release", f"{b}:refs/heads/staging")
        hook = self.repo / ".git/hooks/pre-push"
        hook.write_text(f'#!/bin/sh\ngit --git-dir="$2" update-ref refs/heads/master {b} {self.a}\n')
        hook.chmod(0o755)
        result = self.cleanup()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.tip("master"), b)
        self.assertEqual(self.tip("main"), self.a)

    def test_missing_remote_main_does_not_use_stale_tracking_ref(self):
        self.remote_git("update-ref", "-d", "refs/heads/main")
        self.assertNotEqual(self.cleanup().returncode, 0)
        self.assertEqual(self.tip("master"), self.a)

    def test_unreachable_remote_blocks_cleanup(self):
        self.git("remote", "set-url", "release", str(self.root / "missing.git"))
        self.assertNotEqual(self.cleanup().returncode, 0)
        self.assertEqual(self.tip("master"), self.a)


class ResourceLinksTest(unittest.TestCase):
    def test_relative_markdown_resources_exist(self):
        # Check executable examples and references stay discoverable after prose refactoring.
        for source in [ROOT / "README.md", ROOT / "docs/setup.md", *(ROOT / "skills").rglob("*.md")]:
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", source.read_text()):
                if "://" in target or target.startswith("#"):
                    continue
                with self.subTest(source=source, target=target):
                    self.assertTrue((source.parent / target.split("#", 1)[0]).is_file())


if __name__ == "__main__":
    unittest.main()
