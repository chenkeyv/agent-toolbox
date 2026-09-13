# Repository Agent Instructions

This repository is an Agent Plugins 1.0 package for reusable skills, prompts, MCP examples,
and memory templates. The repository root is the plugin root.

When changing this repo:

- Keep the portable manifest at root `plugin.json` and target the published Agent Plugins schema.
- Keep client adapters optional. Add a marketplace entry or client manifest only when a target
  client's documented installation, distribution, or runtime requirements justify it. Document
  the target and validate the adapter without replacing root `plugin.json` or copying skills.
- Keep the package skills-first. Do not add framework-neutral agent rosters, team
  indexes, or placeholder subagent scaffolding unless a runtime integration is
  intentionally introduced.
- Prefer Markdown for human-readable instructions and YAML or JSON for structured metadata.
- Add reusable Agent Skills under `skills/<skill-name>/SKILL.md`.
- Add prompt templates under `prompts/`.
- Add MCP examples under `mcp/`, but never commit tokens or local credentials. Add root `mcp.json`
  only when the plugin actually provides runnable MCP servers.
- Keep reusable memory templates under `memory/` and follow `memory/schema.yaml` for new entries.
- Do not store secrets, credentials, private personal details, or unverifiable claims in memory.
- Update memory only when the information is likely to be useful beyond the current task.
- Avoid binding the repo to one agent framework unless that framework is intentionally added.
- Keep project-specific checkpoints in the project that uses the plugin, not in this repo.
- Update `README.md`, `skills/README.md`, and the portable plugin version whenever the bundled skill
  set changes.
- Use Conventional Commits for Git commit subjects (`type(scope): subject`).
- For multi-line commit messages, use separate `-m` flags or a commit message
  file instead of escaped `\n` in a single `-m` argument.
- Run plugin validation before committing package changes.
