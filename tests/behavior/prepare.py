"""Create raw, offline fixtures for a fresh agent evaluation session."""

import argparse
from pathlib import Path
import subprocess


def git(path, *args):
    return subprocess.run(["git", "-C", str(path), *args], check=True, text=True,
                          capture_output=True).stdout.strip()


def write(root, name, text):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def repository(path):
    path.mkdir(parents=True)
    git(path, "init", "-q", "-b", "master")
    git(path, "config", "user.name", "Evaluation")
    git(path, "config", "user.email", "evaluation@example.invalid")
    git(path, "config", "commit.gpgsign", "false")


def checkpoint(path, message):
    git(path, "add", ".")
    git(path, "commit", "-q", "--allow-empty", "-m", message)


def prepare(root):
    root.mkdir(parents=True, exist_ok=False)
    project = root / "project"
    repository(project)
    write(project, "README.md", """# Maple schema checker

This Python standard-library project validates synthetic schema fixtures.
Run `python3 -m unittest discover -s tests` for behavior changes.
`schemas/` is maintained by this project. No pytest dependency is installed.
Local agent skills live in `.agents/skills/` and `.claude/skills/`.
""")
    write(project, "AGENTS.md", """# Project instructions

Run `pytest` for behavior changes.
Keep schema fixtures synthetic and preserve field names consumed by clients.
""")
    write(project, "AGENTS.override.md", """Use Python's unittest runner as documented in README.md.
Preserve existing local skill files and `.agent-memory/`; they are maintained separately.
""")
    write(project, "CLAUDE.md", "Run `python3 -m unittest discover -s tests` after behavior changes.\n")
    write(project, ".gitignore", ".agents/\n.claude/\n.agent-memory/\n__pycache__/\n")
    write(project, ".agents/skills/check-schema/SKILL.md", """---
name: check-schema
description: Check changes to Maple schema fixtures for field-name compatibility.
---
Compare changed fields with `schemas/sample.json`. Preserve client-visible field names.
""")
    write(project, ".claude/skills/check-schema/SKILL.md",
          (project / ".agents/skills/check-schema/SKILL.md").read_text())
    write(project, ".agent-memory/project.md", "Local owner: maintainer. Schema format remains v1.\n")
    write(project, "schemas/sample.json", '{"version": 1, "fields": ["name"]}\n')
    write(project, "tests/test_schema.py", """import json
from pathlib import Path
import unittest

class SchemaTest(unittest.TestCase):
    def test_required_client_field(self):
        schema = json.loads(Path('schemas/sample.json').read_text())
        self.assertIn('name', schema['fields'])
""")
    checkpoint(project, "Initial project")

    diagnostic = root / "diagnostic"
    diagnostic.mkdir()
    write(diagnostic, "evidence.txt", """The project has an instruction to run its test command before delivery.
The previous response said 'done' and did not report test results.
The instruction file exists now. The earlier session's loading trace, tool calls,
and command logs are unavailable.
""")

    audit = root / "audit"
    repository(audit)
    write(audit, "skills/check-csv/SKILL.md", """---
name: check-csv
description: Validate an exported CSV's column names against a user-supplied schema.
---
# Check CSV

Read the supplied schema and CSV header. Report missing or extra columns with the
observed header as evidence. Ask for the schema if it is absent; do not infer it.
Keep the CSV unchanged unless the user requests a correction.
""")
    checkpoint(audit, "Small audit subject")

    migration = root / "migration"
    repository(migration)
    checkpoint(migration, "A")
    git(migration, "branch", "main")
    remote = root / "release.git"
    subprocess.run(["git", "init", "-q", "--bare", str(remote)], check=True)
    git(migration, "remote", "add", "release", str(remote))
    checkpoint(migration, "B on master")
    git(migration, "push", "release", "master")
    git(migration, "switch", "main")
    checkpoint(migration, "C on main")
    git(migration, "push", "release", "main")
    git(remote, "symbolic-ref", "HEAD", "refs/heads/main")
    decoy = root / "origin.git"
    subprocess.run(["git", "clone", "-q", "--bare", str(remote), str(decoy)], check=True)
    git(migration, "remote", "add", "origin", str(decoy))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="New directory outside the package checkout")
    prepare(parser.parse_args().destination.resolve())
