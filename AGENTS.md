# Repository Agent Instructions

This repository is a private Codex plugin marketplace for reusable skills, prompts,
MCP examples, memory templates, and plugin packaging.

When changing this repo:

- Keep the marketplace catalog at `.agents/plugins/marketplace.json`.
- Keep the installable Agent Toolbox package under `plugins/agent-toolbox/`.
- Keep the package skills-first. Do not add framework-neutral agent rosters, team
  indexes, or placeholder subagent scaffolding unless a runtime integration is
  intentionally introduced.
- Prefer Markdown for human-readable instructions and YAML or JSON for structured metadata.
- Add reusable Codex skills under `plugins/agent-toolbox/skills/<skill-name>/SKILL.md`.
- Add prompt templates under `plugins/agent-toolbox/prompts/`.
- Add MCP examples under `plugins/agent-toolbox/mcp/`, but never commit tokens or local credentials.
- Keep reusable memory templates under `plugins/agent-toolbox/memory/` and follow `plugins/agent-toolbox/memory/schema.yaml` for new entries.
- Do not store secrets, credentials, private personal details, or unverifiable claims in memory.
- Update memory only when the information is likely to be useful beyond the current task.
- Avoid binding the repo to one agent framework unless that framework is intentionally added.
- Keep project-specific checkpoints in the project that uses the plugin, not in this repo.
- Update `plugins/agent-toolbox/README.md`, `plugins/agent-toolbox/skills/README.md`,
  and the plugin cachebuster whenever the bundled skill set changes.
- Use Conventional Commits for Git commit subjects (`type(scope): subject`).
- For multi-line commit messages, use separate `-m` flags or a commit message
  file instead of escaped `\n` in a single `-m` argument.
- Run plugin validation before committing package changes.
