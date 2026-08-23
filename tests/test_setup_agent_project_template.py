from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
GUIDE_PATH = ROOT / "skills/setup-agent-project/references/agents-template.md"
GUIDE_REFERENCE_PATHS = [
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

REQUIRED_CHINESE_WRITING_RULES = [
    "使用自然、规范、符合中文语法习惯的表达",
    "避免照搬英文句式和明显的翻译腔",
    "不生造词语，不为了显得专业而使用少见、晦涩或不必要的表达",
    "避免不必要的互联网、商业和职场黑话",
    "深钻",
    "下挖",
    "口径",
    "抓手",
    "拉通",
    "对齐",
    "颗粒度",
    "如果有常见、准确的中文表达，优先使用常见表达",
    "技术术语可以保留，但解释和叙述应尽量使用自然中文",
]


def normalize(text):
    return " ".join(text.split())


class SetupAgentProjectTailoringGuideTest(unittest.TestCase):
    def test_includes_required_working_rules(self):
        text = normalize(GUIDE_PATH.read_text())
        for rule in REQUIRED_RULES:
            with self.subTest(rule=rule):
                self.assertIn(normalize(rule), text)

    def test_includes_required_chinese_writing_rules(self):
        text = normalize(GUIDE_PATH.read_text())
        self.assertIn("## Candidate Chinese Writing Rules", GUIDE_PATH.read_text())
        for rule in REQUIRED_CHINESE_WRITING_RULES:
            with self.subTest(rule=rule):
                self.assertIn(normalize(rule), text)

    def test_skill_and_guide_reference_the_tailoring_guide(self):
        for path, reference in GUIDE_REFERENCE_PATHS:
            text = path.read_text()
            with self.subTest(path=path):
                self.assertIn(reference, text)
                self.assertNotIn("\n# Agent Project Instructions\n", text)
                self.assertNotIn("\n## Agent Toolbox Setup\n", text)

        setup_guide = normalize((ROOT / "docs/setup.md").read_text())
        self.assertIn("rule catalog, not a file template", setup_guide)
        self.assertNotIn("canonical", setup_guide)

    def test_guide_is_not_a_copy_ready_agents_file(self):
        guide = GUIDE_PATH.read_text()
        normalized_guide = normalize(guide)

        self.assertIn("Do not copy this file into a project", guide)
        self.assertIn("written from repository evidence", normalized_guide)
        self.assertIn("not a wholesale or near-wholesale copy", normalized_guide)
        self.assertNotIn("```md\n# Agent Project Instructions", guide)
        self.assertNotIn("## Project-Specific Rules", guide)
        self.assertNotIn("Add repository-specific build", guide)

    def test_skill_requires_evidence_driven_tailoring(self):
        skill = normalize((ROOT / "skills/setup-agent-project/SKILL.md").read_text())

        self.assertIn("Draft the project-specific sections from inspected repository evidence", skill)
        self.assertIn("Omit generic rules already supplied by higher-scope instructions", skill)
        self.assertIn("not a wholesale or near-wholesale copy", skill)

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
