---
name: setup-agent-project
description: Set up, refresh, or repair a repository for agent-assisted work, especially skills-first Agent Toolbox workflows. Use when the user asks to configure or update a project for coding agents, add or refresh project instructions, install or reference Agent Toolbox, create project-owned memory or checkpoints, add project-owned skills, verify an existing setup, or make agent configuration idempotent.
---

# Setup Agent Project

Make a repository ready for agent-assisted work while keeping reusable skills, project-owned state,
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
   - Use the active client's project-owned skills directory when behavior belongs to this
     repository; `.agents/skills/` is appropriate only when that client supports it.
   - Do not add a framework-neutral agent roster, placeholder subagent configuration, or Git
     submodule unless the user explicitly wants that runtime or external upstream.
   - Keep project-specific checkpoints, learning state, and private local notes in the project, not
     inside Agent Toolbox or another reusable bundle.

3. Add or update root project instructions.
   - Keep the active client's project instruction file concise and project-specific; use root
     `AGENTS.md` when the client supports it.
   - State how the project should use installed or project-owned skills.
   - State where durable project memory belongs.
   - State that current user instructions and repository files override bundled skill guidance or
     older memory.
   - State the secrets policy: do not commit tokens, credentials, OAuth state, or machine-local
     configuration.
   - Put refreshable Agent Toolbox guidance inside an `agent-toolbox` managed block.
   - Preserve existing project rules unless the user asks to replace them.

4. Add project-owned memory only when explicitly requested.
   - Create paths such as `.agent-memory/project.md`, `docs/agent-memory.md`, or
     `learning/<topic>.md` only when the user explicitly asks for durable memory or checkpoints.
   - If persistent memory would help but was not requested, recommend a destination without
     creating or updating memory files.
   - Record source, owner, confidence, and update date when practical.
   - Do not store secrets, private personal details, or unverifiable claims.

5. Add project-owned skills only when needed.
   - Use one directory per skill under the active client's project-owned skills location.
   - Add a `SKILL.md` with `name` and `description` frontmatter and concise task instructions.
   - Add scripts, references, or assets only when they materially support the workflow.
   - Prefer the skill-creator workflow when available and validate every new or changed skill.

6. Verify the setup.
   - Run `git status --short --branch` and inspect the complete diff.
   - If a submodule was explicitly requested, run `git submodule status` and inspect `.gitmodules`.
   - If the Agent Toolbox plugin package changed, run its skill and package validation commands.
   - Report installed or changed files, verification performed, and any client-specific reload or
     new-task step required for the change to take effect.

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

Prefer installing the repository root as an Agent Plugins 1.0 package over vendoring individual
skills. Installation, distribution, enablement, and update flows are client-specific, so follow the
active client's Agent Plugins instructions and point it at the directory containing `plugin.json`.

Do not add a Codex marketplace wrapper or `.codex-plugin` manifest merely to expose Agent Toolbox.
Add client-specific packaging only when the user explicitly needs a capability outside the portable
Agent Plugins format. After installing or updating, report any client-specific reload or new-task
step required to load the bundled skills.

## Project-Owned Skill Assets

Keep repository-specific reusable behavior local when it should not ship in the plugin:

```text
<client-project-skills>/
  example-skill/
    SKILL.md
```

Use a Git submodule only when the user explicitly asks to track an external upstream repository.
If a submodule is needed, let Git create or update `.gitmodules` instead of editing it manually.

## AGENTS.md Template

When the active client supports root `AGENTS.md` and the project needs one, read
[the canonical template](references/agents-template.md) and tailor it to the target repository.
Keep the managed block idempotent and preserve project-specific rules outside it.
