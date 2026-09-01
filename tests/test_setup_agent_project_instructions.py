from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = ROOT / "skills/setup-agent-project/SKILL.md"
DOCS_PATH = ROOT / "docs/setup.md"
EXAMPLE_PATH = ROOT / "skills/setup-agent-project/references/agents-example.md"
REVIEW_PATH = ROOT / "skills/setup-agent-project/references/agents-content-review.md"
OLD_TEMPLATE_PATH = ROOT / "skills/setup-agent-project/references/agents-template.md"

EXPECTED_LEGACY_REVIEW_CONCEPTS = {
    "chinese.common": ("common, accurate Chinese",),
    "chinese.natural": ("natural, standard Chinese", "common Chinese grammar"),
    "chinese.no-invented": ("invented, obscure",),
    "chinese.no-jargon": ("workplace jargon", "深钻"),
    "chinese.no-translationese": ("English sentence patterns", "translationese"),
    "chinese.technical-terms": ("accurate technical terms", "explanations"),
    "git.conventional": ("Conventional Commit subjects",),
    "git.multiline": ("separate `-m` flags", "message file"),
    "git.split": ("logically independent changes", "review or rollback"),
    "git.wrap-72": ("72 characters",),
    "instructions.precedence": ("current user instructions", "reusable skill guidance"),
    "memory.project-owned": ("project memory or checkpoints", "repository"),
    "memory.provenance": ("provenance requirement",),
    "secrets.no-commit": ("committing secrets", "OAuth state"),
    "skills.match": ("particular installed or project-owned skill",),
    "skills.no-multi-agent-assumption": ("multi-agent runtime",),
    "skills.project-owned": ("real directory", "ownership boundary"),
    "tests.add-or-explain": ("what to test", "cannot practically be added"),
    "tests.root-cause": ("cause of every failing test",),
    "tooling.no-vendor": ("vendoring or cloning reusable tooling",),
    "validation.relevant": ("most relevant validation", "skipped"),
    "workflow.assumptions": ("assumptions", "evidence is unavailable"),
    "workflow.evidence": ("file references", "command output"),
    "workflow.inspect-status": ("Git status", "existing project guidance"),
    "workflow.scoped-edits": ("edits scoped", "unrelated changes"),
}


def normalize(text):
    return " ".join(text.split())


def section(text, start_heading, end_heading):
    return text.split(start_heading, 1)[1].split(end_heading, 1)[0]


class SetupAgentProjectGenerationTest(unittest.TestCase):
    def test_example_is_concrete_but_not_a_copy_source(self):
        example = EXAMPLE_PATH.read_text()
        normalized = normalize(example)

        self.assertIn("fictional repository", normalized)
        self.assertIn("not a template, base, checklist, or source of wording", normalized)
        self.assertIn("crates/lantern-core", example)
        self.assertIn("cargo test --workspace", example)
        self.assertNotIn("<!-- agent-toolbox:start -->", example)
        self.assertFalse(OLD_TEMPLATE_PATH.exists())

    def test_review_runs_only_after_an_independent_draft(self):
        review = normalize(REVIEW_PATH.read_text())
        skill = normalize(SKILL_PATH.read_text())

        self.assertIn("only after an independent first draft is complete", review)
        self.assertIn("missed categories of project facts", review)
        self.assertIn("return to the target repository or the user's request for evidence", review)
        self.assertIn("Only after the independent first draft is complete", skill)
        self.assertIn("do not copy the review's structure or wording", skill)

    def test_review_retains_all_previous_template_rule_concepts(self):
        review = REVIEW_PATH.read_text()
        pattern = re.compile(
            r"<!-- legacy-review: (?P<id>[a-z0-9.-]+) -->\s*(?P<body>.*?)"
            r"(?=\n<!-- legacy-review:|\n## |\Z)",
            re.DOTALL,
        )
        actual = {
            match.group("id"): normalize(match.group("body"))
            for match in pattern.finditer(review)
        }

        self.assertEqual(set(EXPECTED_LEGACY_REVIEW_CONCEPTS), set(actual))
        for review_id, expected_terms in EXPECTED_LEGACY_REVIEW_CONCEPTS.items():
            body = actual[review_id]
            with self.subTest(review_id=review_id):
                self.assertGreaterEqual(len(body), 30)
                self.assertIn("?", body)
                for term in expected_terms:
                    self.assertIn(term.lower(), body.lower())

    def test_refresh_contract_covers_the_whole_instruction_file(self):
        skill_refresh = normalize(
            section(
                SKILL_PATH.read_text(),
                "## Refresh Existing Projects",
                "## Agent Toolbox Plugin Setup",
            )
        )
        docs_refresh = normalize(
            section(DOCS_PATH.read_text(), "## Refresh Existing Projects", "## Use The Skills")
        )

        for refresh in (skill_refresh, docs_refresh):
            with self.subTest(refresh=refresh):
                self.assertIn("entire project instruction file", refresh)
                self.assertIn("outside any managed block", refresh)
                self.assertIn("ownership boundary", refresh)
                self.assertIn("second refresh", refresh)

    def test_final_review_requires_evidence_backed_additions(self):
        review = normalize(REVIEW_PATH.read_text())

        self.assertNotIn("deleting both reference files", review)
        self.assertIn("review-driven additions", review)
        self.assertIn("independently from repository evidence", review)
        self.assertIn("repository has no project-owned agent assets", review)

    def test_skill_requires_free_generation(self):
        skill = normalize(SKILL_PATH.read_text())

        self.assertIn("Generate the instruction file freely", skill)
        self.assertIn(
            "do not start from a template, reference checklist, or fixed set of sections",
            skill,
        )
        self.assertIn("not sufficient reason to add such a block", skill)
        self.assertIn(
            "independently generated rather than copied or adapted from the example",
            skill,
        )

    def test_skill_removes_generic_managed_blocks(self):
        refresh = normalize(
            section(
                SKILL_PATH.read_text(),
                "## Refresh Existing Projects",
                "## Agent Toolbox Plugin Setup",
            )
        )

        self.assertIn("remove generic or inherited advice", refresh)
        self.assertIn("remove the markers when no owned content remains", refresh)

    def test_skill_and_docs_reference_example_and_review(self):
        skill = SKILL_PATH.read_text()
        docs = DOCS_PATH.read_text()

        self.assertIn("references/agents-example.md", skill)
        self.assertIn("references/agents-content-review.md", skill)
        self.assertIn("../skills/setup-agent-project/references/agents-example.md", docs)
        self.assertIn("../skills/setup-agent-project/references/agents-content-review.md", docs)
        self.assertNotIn("agents-template.md", skill)
        self.assertNotIn("agents-template.md", docs)

    def test_safety_boundaries_are_explicit(self):
        rename_text = normalize((ROOT / "skills/rename-master-to-main/SKILL.md").read_text())
        setup_text = normalize(SKILL_PATH.read_text())

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
