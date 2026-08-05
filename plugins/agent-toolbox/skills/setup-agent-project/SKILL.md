---
name: setup-agent-project
description: Set up, refresh, or repair a repository for Codex-assisted work, especially skills-first Agent Toolbox workflows. Use when the user asks to configure or update a project for Codex, add or refresh AGENTS.md instructions, install or reference Agent Toolbox, create project-owned memory or checkpoints, add project-owned skills under .agents/skills, verify an existing setup, or make agent configuration idempotent.
---

# Setup Agent Project

Make a repository ready for Codex-assisted work while keeping reusable skills, project-owned state,
and secrets in the right places.

## Workflow

1. Inspect the target repository before changing files.
   - Run `git status --short --branch`.
   - Find existing guidance with `rg --files -g 'AGENTS.md' -g '.gitmodules' -g '.agents/**' -g '.agent-memory/**' -g 'learning/**' -g 'docs/**'`.
   - Read the root `AGENTS.md`, `README.md`, `.gitignore`, `.gitmodules`, and existing skill or
     memory files only when present and relevant.
   - Preserve unrelated local changes.

2. Choose the setup model.
   - Prefer the installed Agent Toolbox plugin when the project only needs its reusable skills.
   - Use project-owned skills under `.agents/skills/` when behavior belongs to this repository.
   - Do not add a framework-neutral agent roster, placeholder subagent configuration, or Git
     submodule unless the user explicitly wants that runtime or external upstream.
   - Keep project-specific checkpoints, learning state, and private local notes in the project, not
     inside Agent Toolbox or another reusable bundle.

3. Add or update root project instructions.
   - Keep `AGENTS.md` concise and project-specific.
   - State how the project should use installed or project-owned skills.
   - State where durable project memory belongs.
   - State that current user instructions and repository files override bundled skill guidance or
     older memory.
   - State the secrets policy: do not commit tokens, credentials, OAuth state, or machine-local
     configuration.
   - Put refreshable Agent Toolbox guidance inside an `agent-toolbox` managed block.
   - Preserve existing project rules unless the user asks to replace them.

4. Add project-owned memory only when useful.
   - Create paths such as `.agent-memory/project.md`, `docs/agent-memory.md`, or
     `learning/<topic>.md` when the user asks for durable checkpoints or the setup needs a clear
     memory destination.
   - Record source, owner, confidence, and update date when practical.
   - Do not store secrets, private personal details, or unverifiable claims.

5. Add project-owned skills only when needed.
   - Use one directory per skill under `.agents/skills/<skill-name>/`.
   - Add a `SKILL.md` with `name` and `description` frontmatter and concise task instructions.
   - Add scripts, references, or assets only when they materially support the workflow.
   - Prefer the skill-creator workflow when available and validate every new or changed skill.

6. Verify the setup.
   - Run `git status --short --branch` and inspect the complete diff.
   - If a submodule was explicitly requested, run `git submodule status` and inspect `.gitmodules`.
   - If the Agent Toolbox plugin package changed, run its skill and package validation commands.
   - Report installed or changed files, verification performed, and manual follow-up such as
     reinstalling the plugin or starting a new Codex thread.

## Refresh Existing Projects

Treat repeated runs as idempotent refreshes.

1. Record whether `AGENTS.md`, `.gitmodules`, `.agents/skills/`, `.agent-memory/`, `learning/`, and
   relevant docs already exist.
2. Replace only the content between `<!-- agent-toolbox:start -->` and
   `<!-- agent-toolbox:end -->` when those markers exist.
3. If the markers are absent but a clear Agent Toolbox section exists, wrap and normalize only
   that section. Otherwise add one managed block without rewriting project-specific rules.
4. Stop and ask when existing instructions conflict with the managed block or local assets have an
   unclear owner or external-upstream relationship.
5. Re-read the result and confirm a second refresh would produce no diff.

## Agent Toolbox Plugin Setup

Prefer plugin installation over vendoring reusable skills:

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

## Project-Owned Skill Assets

Keep repository-specific reusable behavior local when it should not ship in the plugin:

```text
.agents/
  skills/
    example-skill/
      SKILL.md
```

Use a Git submodule only when the user explicitly asks to track an external upstream repository.
If a submodule is needed, let Git create or update `.gitmodules` instead of editing it manually.

## AGENTS.md Template

Use this as a starting point, then tailor it to the target project:

```md
# Codex Project Instructions

<!-- agent-toolbox:start -->
## Agent Toolbox Setup

- This repository uses the installed Agent Toolbox Codex plugin or project-owned skills under `.agents/skills/`.
- Use task-specific skills when their descriptions match. Do not assume Agent Toolbox provides a multi-agent runtime.
- Current user instructions and current repository files take precedence over bundled skill guidance and memory templates.

## Project Memory

- Keep durable project memory in `.agent-memory/project.md`, `docs/agent-memory.md`, or a topic-specific file such as `learning/<topic>.md`.
- Keep project-specific checkpoints in this repository, not inside reusable tooling.
- Store only durable, useful context with provenance when practical.

## Working Rules

- Start by inspecting `git status --short --branch` and existing project instructions before changing files.
- Keep edits scoped to the requested setup and preserve unrelated local changes.
- Back every conclusion, recommendation, and summary with real evidence such as
  file references, command output, tests, experiments, source links, or
  measured data.
- Clearly label assumptions when evidence is unavailable.
- Do not commit secrets, credentials, OAuth state, or machine-local configuration.
- Do not vendor or clone reusable tooling into this repository unless plugin installation is unavailable or the user explicitly wants local skills.
- Keep repository-specific skills under `.agents/skills/`.
- Add or update tests with every change. If a test cannot be added, state the
  reason and what validation was run instead.
- When tests fail, identify the root cause before changing or dismissing the
  result, even if the failing case appears unrelated.
- When creating or amending Git commits, use Conventional Commits format
  (`type(scope): subject`).
- Split large or logically separate changes into multiple commits when that
  makes review or rollback clearer.
- Keep Git commit message lines wrapped at 72 characters when practical.
- For multi-line or multi-paragraph commit messages, preserve line breaks with
  separate `-m` flags or a commit message file instead of escaped `\n` in a
  single `-m` argument.
- Run the most relevant validation after setup changes and report any checks that were skipped.
<!-- agent-toolbox:end -->

## Project-Specific Rules

- Add repository-specific build, test, lint, release, and ownership rules here.
```
