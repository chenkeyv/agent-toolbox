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
   - Generate the instruction file freely from the user's request and inspected repository
     evidence. Choose its structure and wording for the target project; do not start from a
     template, reference checklist, or fixed set of sections.
   - Only after the independent first draft is complete, use the content review to check whether it
     missed a category of project facts. If it reveals a gap, return to repository evidence and
     write from that evidence; do not copy the review's structure or wording.
   - Add skill-usage guidance only when this repository has a project-specific workflow for an
     installed or project-owned skill. Add a project-memory section only when memory already exists
     or the user explicitly requested it.
   - Tailor secrets guidance to the repository's actual risk surfaces while retaining the baseline
     prohibition on committing credentials, OAuth state, or machine-local configuration.
   - Omit generic rules already supplied by higher-scope instructions unless this repository needs
     a deliberate override or a project-specific version.
   - Add an `agent-toolbox` managed block only when the repository needs project-specific Agent
     Toolbox guidance that should be refreshed later. Using this skill or the installed plugin is
     not sufficient reason to add such a block.
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
     inherited duplicates, generic workflow advice, and placeholder headings that have no such
     basis.
   - Confirm the result was independently generated rather than copied or adapted from the example,
     and that any commands, paths, privacy boundaries, or ownership statements are real for the
     target project.
   - If a submodule was explicitly requested, run `git submodule status` and inspect `.gitmodules`.
   - If the Agent Toolbox plugin package changed, run its skill and package validation commands.
   - Report installed or changed files, verification performed, and any client-specific reload or
     new-task step required for the change to take effect.

## Refresh Existing Projects

Treat repeated runs as idempotent refreshes.

1. Record whether `AGENTS.md`, `.gitmodules`, `.agents/skills/`, `.agent-memory/`, `learning/`, and
   relevant docs already exist.
2. Re-evaluate the entire project instruction file against the current repository and user request.
   Update stale project-specific commands, paths, boundaries, and ownership statements wherever
   they appear, including outside any managed block. Preserve instructions that remain accurate and
   avoid structure or wording churn that does not improve correctness.
3. Treat `<!-- agent-toolbox:start -->` and `<!-- agent-toolbox:end -->` only as an ownership
   boundary for project-specific Agent Toolbox workflow guidance. Refresh that content when the
   markers exist, remove generic or inherited advice, and remove the markers when no owned content
   remains.
4. If the markers are absent but a clearly Agent Toolbox-owned, project-specific section exists,
   wrap and normalize only that section. Otherwise do not add a managed block.
5. Stop and ask when existing instructions conflict or when content, local assets, or an external
   upstream have unclear ownership.
6. Apply the content review to the refreshed draft, return to repository evidence for any gap it
   exposes, then confirm a second refresh would produce no diff.

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

## AGENTS.md Example and Content Review

When the active client supports root `AGENTS.md` and the project needs one, generate it independently
from the target repository. [The example](references/agents-example.md) is optional and illustrates
only the level of project specificity a finished file can have. Do not use it as a template,
starting point, checklist, section list, or source of wording.

After the first draft is complete, use [the content review](references/agents-content-review.md) to
check whether a category of project facts was missed. The review may trigger more repository
inspection, but it must not determine the file's structure or wording.
