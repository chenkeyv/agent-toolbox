from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATHS = [
    ROOT / "plugins/agent-toolbox/skills/setup-agent-project/SKILL.md",
    ROOT / "plugins/agent-toolbox/docs/setup.md",
]

REQUIRED_RULES = [
    "Back every conclusion, recommendation, and summary with real evidence",
    "file references, command output, tests, experiments, source links, or measured data",
    "Add or update tests with every change",
    "When tests fail, identify the root cause",
    "When creating or amending Git commits, use Conventional Commits format",
    "Split large or logically separate changes into multiple commits",
    "For multi-line or multi-paragraph commit messages, preserve line breaks",
]


def normalize(text):
    return " ".join(text.split())


class SetupAgentProjectTemplateTest(unittest.TestCase):
    def test_includes_required_working_rules(self):
        for path in TEMPLATE_PATHS:
            text = normalize(path.read_text())
            for rule in REQUIRED_RULES:
                with self.subTest(path=path, rule=rule):
                    self.assertIn(normalize(rule), text)


if __name__ == "__main__":
    unittest.main()
