# Repository Agent Instructions

This repository is a private Codex plugin marketplace for reusable agent profiles,
workflows, skills, prompts, and plugin packaging.

When changing this repo:

- Keep the marketplace catalog at `.agents/plugins/marketplace.json`.
- Keep the installable Agent Toolbox package under `plugins/agent-toolbox/`.
- Keep agent definitions practical, concise, and reusable across runtimes.
- Prefer Markdown for human-readable profiles and YAML for structured indexes.
- Add new agents under `plugins/agent-toolbox/agents/` with front matter containing `id`, `name`, and `type`.
- Add reusable Codex skills under `plugins/agent-toolbox/skills/<skill-name>/SKILL.md`.
- Add prompt templates under `plugins/agent-toolbox/prompts/`.
- Add MCP examples under `plugins/agent-toolbox/mcp/`, but never commit tokens or local credentials.
- Keep workflows under `plugins/agent-toolbox/workflows/` and describe handoffs, outputs, and acceptance checks.
- Keep reusable memory templates under `plugins/agent-toolbox/memory/` and follow `plugins/agent-toolbox/memory/schema.yaml` for new entries.
- Do not store secrets, credentials, private personal details, or unverifiable claims in memory.
- Update memory only when the information is likely to be useful beyond the current task.
- Avoid binding the repo to one agent framework unless that framework is intentionally added.
- Keep project-specific checkpoints in the project that uses the plugin, not in this repo.
- Update `plugins/agent-toolbox/README.md`, `plugins/agent-toolbox/team.yaml`, and `plugins/agent-toolbox/memory/agents/` whenever the roster changes.
- Run plugin validation before committing package changes.
