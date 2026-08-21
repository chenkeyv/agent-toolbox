from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "skills/setup-agent-project/references/agents-template.md"
TEMPLATE_REFERENCE_PATHS = [
    (ROOT / "skills/setup-agent-project/SKILL.md", "references/agents-template.md"),
    (
        ROOT / "docs/setup.md",
        "../skills/setup-agent-project/references/agents-template.md",
    ),
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
        text = normalize(TEMPLATE_PATH.read_text())
        for rule in REQUIRED_RULES:
            with self.subTest(rule=rule):
                self.assertIn(normalize(rule), text)

    def test_skill_and_guide_reference_the_canonical_template(self):
        for path, reference in TEMPLATE_REFERENCE_PATHS:
            text = path.read_text()
            with self.subTest(path=path):
                self.assertIn(reference, text)
                self.assertNotIn("\n# Agent Project Instructions\n", text)
                self.assertNotIn("\n## Agent Toolbox Setup\n", text)

    def test_safety_boundaries_are_explicit(self):
        rename_text = normalize((ROOT / "skills/rename-master-to-main/SKILL.md").read_text())
        setup_text = normalize((ROOT / "skills/setup-agent-project/SKILL.md").read_text())

        self.assertIn(
            normalize(
                "For local-only scope, do not fetch, push, change the remote default branch, "
                "or delete remote `master`"
            ),
            rename_text,
        )
        self.assertIn("only when explicitly requested", setup_text)
        self.assertIn("recommend a destination without creating or updating memory files", setup_text)


if __name__ == "__main__":
    unittest.main()
