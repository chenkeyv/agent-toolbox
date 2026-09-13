import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT
PORTABLE_MANIFEST = PACKAGE / "plugin.json"

EXPECTED_SKILLS = [
    "audit-agent-assets",
    "prevent-repeat",
    "rename-master-to-main",
    "setup-agent-project",
]

PORTABLE_MANIFEST_FIELDS = {
    "$schema",
    "name",
    "version",
    "description",
    "author",
    "homepage",
    "repository",
    "license",
    "keywords",
    "extensions",
}

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
    PORTABLE_MANIFEST,
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
        for path in CATALOG_PATHS:
            text = path.read_text()
            with self.subTest(path=path):
                for skill in EXPECTED_SKILLS:
                    self.assertIn(f"| `{skill}` |", text)
                self.assertNotIn("| `agent-toolbox` |", text)

    def test_multi_agent_scaffolding_is_removed(self):
        for path in REMOVED_MULTI_AGENT_PATHS:
            with self.subTest(path=path):
                self.assertFalse(path.exists())

    def test_portable_agent_plugins_manifest(self):
        manifest = json.loads(PORTABLE_MANIFEST.read_text())

        self.assertEqual(
            manifest["$schema"],
            "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        )
        self.assertEqual(manifest["name"], "agent-toolbox")
        self.assertRegex(
            manifest["name"],
            re.compile(r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$"),
        )
        self.assertLessEqual(len(manifest["name"]), 64)
        self.assertLessEqual(set(manifest), PORTABLE_MANIFEST_FIELDS)
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertIsInstance(manifest["description"], str)
        self.assertIsInstance(manifest["author"], dict)
        self.assertLessEqual(set(manifest["author"]), {"name", "email", "url"})
        self.assertTrue(all(isinstance(keyword, str) for keyword in manifest["keywords"]))
        self.assertNotIn("skills", manifest)

    def test_portable_skills_use_fixed_discovery_location(self):
        discovered_skills = sorted(
            path.parent.name
            for path in (PACKAGE / "skills").glob("*/SKILL.md")
            if path.is_file()
        )

        self.assertEqual(discovered_skills, EXPECTED_SKILLS)


if __name__ == "__main__":
    unittest.main()
