# Repository Agent Instructions

This repository stores reusable agent profiles and workflows.

When changing this repo:

- Keep agent definitions practical, concise, and reusable across runtimes.
- Prefer Markdown for human-readable profiles and YAML for structured indexes.
- Add new agents under `agents/` with front matter containing `id`, `name`, and `type`.
- Keep workflows under `workflows/` and describe handoffs, outputs, and acceptance checks.
- Avoid binding the repo to one agent framework unless that framework is intentionally added.
- Update `README.md` and `team.yaml` whenever the roster changes.

