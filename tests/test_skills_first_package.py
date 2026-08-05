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


class SkillsFirstPackageTest(unittest.TestCase):
    def test_learning_coach_is_a_standalone_skill(self):
        self.assertTrue((PACKAGE / "skills/learning-coach/SKILL.md").is_file())
        self.assertTrue((PACKAGE / "skills/learning-coach/agents/openai.yaml").is_file())

        for path in CATALOG_PATHS:
            text = path.read_text()
            with self.subTest(path=path):
                self.assertIn("| `learning-coach` |", text)
                self.assertNotIn("| `agent-toolbox` |", text)

    def test_multi_agent_scaffolding_is_removed(self):
        for path in REMOVED_MULTI_AGENT_PATHS:
            with self.subTest(path=path):
                self.assertFalse(path.exists())

    def test_manifest_promotes_task_specific_skills(self):
        text = (PACKAGE / ".codex-plugin/plugin.json").read_text()
        self.assertIn("$learning-coach", text)
        self.assertIn("$prevent-repeat", text)
        self.assertIn("$setup-agent-project", text)
        self.assertNotIn("Use Agent Toolbox Learning Coach", text)


if __name__ == "__main__":
    unittest.main()
