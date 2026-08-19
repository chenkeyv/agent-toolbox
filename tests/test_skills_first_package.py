from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "plugins/agent-toolbox"

REMOVED_MULTI_AGENT_PATHS = [
    PACKAGE / "team.yaml",
    PACKAGE / "agents",
    PACKAGE / "workflows",
    PACKAGE / "subagents",
    PACKAGE / "memory/agents",
    PACKAGE / "skills/agent-toolbox",
]

CATALOG_PATHS = [
    PACKAGE / "README.md",
    PACKAGE / "skills/README.md",
]

LEARNING_COACH_REFERENCE_PATHS = [
    PACKAGE / ".codex-plugin/plugin.json",
    PACKAGE / "README.md",
    PACKAGE / "docs/setup.md",
    PACKAGE / "memory/project.md",
    PACKAGE / "skills/README.md",
]


class SkillsFirstPackageTest(unittest.TestCase):
    def test_learning_coach_is_removed(self):
        self.assertFalse((PACKAGE / "skills/learning-coach").exists())

        for path in LEARNING_COACH_REFERENCE_PATHS:
            text = path.read_text().lower()
            with self.subTest(path=path):
                self.assertNotIn("learning-coach", text)
                self.assertNotIn("learning coach", text)

    def test_catalogs_list_remaining_skills(self):
        expected_skills = [
            "prevent-repeat",
            "rename-master-to-main",
            "setup-agent-project",
        ]

        for path in CATALOG_PATHS:
            text = path.read_text()
            with self.subTest(path=path):
                for skill in expected_skills:
                    self.assertIn(f"| `{skill}` |", text)
                self.assertNotIn("| `agent-toolbox` |", text)

    def test_multi_agent_scaffolding_is_removed(self):
        for path in REMOVED_MULTI_AGENT_PATHS:
            with self.subTest(path=path):
                self.assertFalse(path.exists())

    def test_manifest_promotes_task_specific_skills(self):
        text = (PACKAGE / ".codex-plugin/plugin.json").read_text()
        self.assertIn("$prevent-repeat", text)
        self.assertIn("$setup-agent-project", text)


if __name__ == "__main__":
    unittest.main()
