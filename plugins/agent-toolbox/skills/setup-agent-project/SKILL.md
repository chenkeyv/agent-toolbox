---
name: setup-agent-project
description: Set up, refresh, or repair a repository for agent-assisted work, especially Agent Toolbox and Codex workflows. Use when the user asks to configure or update a project for agent workflows, add or refresh AGENTS.md instructions, install or reference Agent Toolbox, create project-owned agent memory/checkpoints, add hidden .agents tooling, organize specialist agent files, verify an agent setup, or make existing agent configuration idempotent.
---

# Setup Agent Project

Use this skill to make a repository ready for agent-assisted work while keeping reusable tooling,
project-owned state, and secrets in the right places.

## Workflow

1. Inspect the target repository before changing files.
   - Run `git status --short --branch`.
   - Find existing guidance with `rg --files -g 'AGENTS.md' -g '.gitmodules' -g '.agents/**' -g 'agents/**' -g '.agent-memory/**' -g 'learning/**' -g 'docs/**'`.
   - Read the root `AGENTS.md`, `README.md`, `.gitignore`, `.gitmodules`, and existing agent or memory files only when present and relevant.
   - Preserve unrelated local changes.

2. Choose the setup model.
   - Prefer the installed Agent Toolbox plugin when the project only needs reusable workflows and skills.
   - Use project-owned files under `.agents/` when the project needs local agent assets.
   - Do not add a Git submodule unless the user explicitly wants to track an external upstream repo.
   - Keep project-specific checkpoints, learning state, and private local notes in the project, not inside Agent Toolbox or another reusable bundle.

3. Add or update root project instructions.
   - Keep `AGENTS.md` concise and project-specific.
   - State how the project should use Agent Toolbox or local agent assets.
   - State where durable project memory belongs.
   - State that current user instructions and current repository files override bundled templates or older memory.
   - State the secrets policy: do not commit tokens, credentials, OAuth state, or machine-local config.
   - Put refreshable Agent Toolbox guidance inside an `agent-toolbox` managed block.
   - Preserve existing project rules unless the user asks to replace them.

4. Add project-owned memory only when useful.
   - Create paths such as `.agent-memory/project.md`, `docs/agent-memory.md`, or `learning/<topic>.md` when the user asks for durable checkpoints or the setup needs a clear memory destination.
   - Record source, owner, confidence, and update date when practical.
   - Do not store secrets, private personal details, or unverifiable claims.

5. Add agent artifacts only when the project needs them.
   - Use Markdown for human-readable agent profiles.
   - Use YAML for structured indexes, rosters, or routing maps.
   - For Agent Toolbox-style profiles, include front matter with `id`, `name`, and `type`.
   - Keep MCP examples token-free and use environment variable placeholders for credentials.

6. Verify the setup.
   - Run `git status --short --branch`.
   - If a submodule is used, run `git submodule status` and inspect `.gitmodules`.
   - If the Agent Toolbox plugin package is changed, run the plugin validation command available in that repo or environment.
   - Report installed or changed files, verification performed, and any manual follow-up such as reinstalling the plugin or starting a new Codex thread.

## Refresh Existing Projects

Treat repeated runs as idempotent refreshes.

1. Build an evidence inventory before editing.
   - Record whether `AGENTS.md`, `.gitmodules`, `.agents/`, `.agent-memory/`,
     `learning/`, and relevant docs already exist.
   - Identify existing project-specific rules and local setup choices.
   - Report the inventory in the final response.

2. Update only refreshable guidance.
   - If `AGENTS.md` contains `<!-- agent-toolbox:start -->` and
     `<!-- agent-toolbox:end -->`, replace only the content between those markers.
   - If the markers are absent but a clear Agent Toolbox section already exists,
     wrap that section in managed markers and normalize only that section.
   - If the markers are absent and no clear section exists, add one managed block in
     the most natural location, usually after the repository context or at the end.
   - Do not rewrite headings, prose, or project-specific rules outside the managed block.
   - Do not duplicate equivalent rules that already exist outside the block; keep the
     managed block concise and note any preserved external rule in the final response.

3. Stop on conflicts.
   - If existing instructions contradict the managed block, report the conflicting
     lines and ask for direction instead of choosing silently.
   - If local agent assets appear to be an embedded repository, report the evidence
     and ask whether the user wants a plain project-owned copy or a real submodule.

4. Verify idempotence.
   - After a refresh, inspect the diff and confirm only intended files changed.
   - State that running the refresh again should produce no diff.
   - If practical, run a second no-op check by re-reading the target file and confirming
     the managed block already matches the template before finishing.

## Agent Toolbox Plugin Setup

Prefer plugin installation over vendoring when the user wants reusable Agent Toolbox behavior:

```bash
codex plugin marketplace add chenkeyv/agent-toolbox --ref main
codex plugin add agent-toolbox@agent-toolbox
```

For local development against a checkout:

```bash
codex plugin marketplace add /path/to/agent-toolbox
codex plugin add agent-toolbox@agent-toolbox
```

After installing or updating the plugin, tell the user to start a new Codex thread so the bundled
skills are loaded.

## Local Agent Assets

When the project needs local agent assets, prefer project-owned files under `.agents/`:

```text
.agents/
  agents/
  workflows/
  memory/
```

Use a Git submodule only when the user explicitly asks to track an external upstream repository.
If a submodule is needed, let Git create or update `.gitmodules` instead of editing it manually.

## AGENTS.md Template

Use this as a starting point, then tailor it to the target project:

```md
# Codex Project Instructions

<!-- agent-toolbox:start -->
## Agent Toolbox Setup

- This repository uses the installed Agent Toolbox Codex plugin or project-owned agent assets under `.agents/`.
- When the user asks to use Agent Toolbox, use the installed plugin skill and follow its bundled team/workflow files.
- Current user instructions and current repository files take precedence over bundled Agent Toolbox memory templates.

## Project Memory

- Keep durable project memory in `.agent-memory/project.md`, `docs/agent-memory.md`, or a topic-specific file such as `learning/<topic>.md`.
- Keep project-specific checkpoints in this repository, not inside reusable agent tooling.
- Store only durable, useful context with provenance when practical.

## Working Rules

- Start by inspecting `git status --short --branch` and existing project instructions before changing files.
- Keep edits scoped to the requested setup and preserve unrelated local changes.
- Back conclusions, recommendations, and summaries with real evidence such as
  file references, command output, tests, source links, or measured data.
- Clearly label assumptions when evidence is unavailable.
- Do not commit secrets, credentials, OAuth state, or machine-local configuration.
- Do not vendor or clone reusable agent tooling into this repository unless plugin installation is unavailable or the user explicitly wants local assets.
- Keep local agent assets as project-owned files under `.agents/` unless the user explicitly asks for an external Git submodule.
- Use Conventional Commits for Git commit subjects (`type(scope): subject`).
- Keep Git commit message lines wrapped at 72 characters when practical.
- For multi-paragraph commit messages, use separate `-m` flags or a commit
  message file instead of escaped `\n` in a single `-m`.
- Run the most relevant validation after setup changes and report any checks that were skipped.
<!-- agent-toolbox:end -->

## Project-Specific Rules

- Add repository-specific build, test, lint, release, and ownership rules here.
```
