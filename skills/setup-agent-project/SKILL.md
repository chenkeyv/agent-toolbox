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
   - Draft the project-specific sections from inspected repository evidence before consulting the
     tailoring guide. Name real products, source boundaries, commands, generated paths, and safety
     constraints instead of retaining generic headings or placeholder text.
   - Add skill-usage guidance only when installed or project-owned skills actually apply. Add a
     project-memory section only when memory already exists or the user explicitly requested it.
   - Tailor secrets guidance to the repository's actual risk surfaces while retaining the baseline
     prohibition on committing credentials, OAuth state, or machine-local configuration.
   - Omit generic rules already supplied by higher-scope instructions unless this repository needs
     a deliberate override or a project-specific version.
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
   - Map every new instruction to an explicit user request or inspected repository evidence. Remove
     generic catalog entries, inherited duplicates, and placeholder headings that have no such
     basis.
   - Confirm the result is not a wholesale or near-wholesale copy of the tailoring guide and that
     its build, test, lint, release, privacy, and ownership statements use the target project's real
     commands and paths when those topics apply.
   - If a submodule was explicitly requested, run `git submodule status` and inspect `.gitmodules`.
   - If the Agent Toolbox plugin package changed, run its skill and package validation commands.
   - Report installed or changed files, verification performed, and any client-specific reload or
     new-task step required for the change to take effect.

## Refresh Existing Projects

Treat repeated runs as idempotent refreshes.

1. Record whether `AGENTS.md`, `.gitmodules`, `.agents/skills/`, `.agent-memory/`, `learning/`, and
   relevant docs already exist.
2. Edit only stale Agent Toolbox-owned content between `<!-- agent-toolbox:start -->` and
   `<!-- agent-toolbox:end -->` when those markers exist. Preserve useful project-specific
   tailoring inside the block; do not replace it with the full guide or candidate-rule catalog.
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

## AGENTS.md Tailoring Guide

When the active client supports root `AGENTS.md` and the project needs one, read
[the tailoring guide](references/agents-template.md) as a completeness check after drafting from
repository evidence. It is a rule catalog, not a file template: select only applicable guidance and
rewrite it around the target project's real structure and commands.
Keep the managed block idempotent and preserve project-specific rules outside it.
