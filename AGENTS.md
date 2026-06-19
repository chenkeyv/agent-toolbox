# Repository Agent Instructions

This repository stores reusable agent profiles, workflows, skills, prompts, and
plugin packaging for Codex and other agent runtimes.

When changing this repo:

- Keep agent definitions practical, concise, and reusable across runtimes.
- Prefer Markdown for human-readable profiles and YAML for structured indexes.
- Add new agents under `agents/` with front matter containing `id`, `name`, and `type`.
- Add reusable Codex skills under `skills/<skill-name>/SKILL.md`.
- Add installable Codex plugin bundles under `plugins/`.
- Add prompt templates under `prompts/`.
- Add MCP examples under `mcp/`, but never commit tokens or local credentials.
- Keep workflows under `workflows/` and describe handoffs, outputs, and acceptance checks.
- Keep persistent memory under `memory/` and follow `memory/schema.yaml` for new entries.
- Do not store secrets, credentials, private personal details, or unverifiable claims in memory.
- Update memory only when the information is likely to be useful beyond the current task.
- Avoid binding the repo to one agent framework unless that framework is intentionally added.
- Keep project-specific checkpoints in the parent project that installs this repo, not in this repo.
- Update `README.md`, `team.yaml`, and `memory/agents/` whenever the roster changes.
