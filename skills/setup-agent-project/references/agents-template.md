# AGENTS.md Tailoring Guide

Do not copy this file into a project. It is a catalog for checking a draft that was already written
from repository evidence. A finished project instruction file should describe that repository, not
the Agent Toolbox template.

## Synthesis Order

1. Inspect the repository instructions, README, manifests, source layout, CI, scripts, and ignore
   rules.
2. Draft only the rules supported by those files or by the user's request. Use exact target names,
   paths, commands, privacy boundaries, generated files, and release steps.
3. Consult the candidate rules below as a completeness check. Select only applicable items and
   rewrite them around the project; do not reproduce every section.
4. Put only refreshable Agent Toolbox-owned guidance between the `agent-toolbox:start` and
   `agent-toolbox:end` comment markers. Keep the rest of the project rules outside that block.

Do not add a project-memory section unless memory already exists or the user requested it. Do not
repeat higher-scope instructions merely because they appear below. Never retain headings such as
"Project-Specific Rules" or instructions to "add rules here" in the finished file.

## Project Evidence To Encode

Use the categories that actually apply:

- What the repository builds and the supported platforms or runtimes.
- Which source directories or packages own domain logic, UI, generated code, tests, and fixtures.
- Exact build, test, lint, format, release, and live-verification commands found in repository files.
- Repository-specific privacy, security, credential, network, or data-handling boundaries.
- Files that are generated, machine-local, externally owned, or intentionally excluded from Git.
- Ownership or release constraints that would be easy to violate without local context.

## Candidate Agent Toolbox Rules

Use these only when the repository actually uses the corresponding capability:

- Use task-specific skills when their descriptions match. Do not assume Agent Toolbox provides a multi-agent runtime.
- Current user instructions and current repository files take precedence over bundled skill guidance and memory templates.
- Keep project-specific checkpoints in this repository, not inside reusable tooling.
- Store only durable, useful context with provenance when practical.
- Do not vendor or clone reusable tooling into this repository unless plugin installation is unavailable or the user explicitly wants local skills.
- Keep repository-specific skills in the active client's project-owned skills directory.

## Candidate Working Rules

Select only rules that are not already inherited and make them concrete where the repository
provides a command or path:

- Start by inspecting `git status --short --branch` and existing project instructions before changing files.
- Keep edits scoped to the requested setup and preserve unrelated local changes.
- Back every conclusion, recommendation, and summary with real evidence such as file references, command output, tests, experiments, source links, or measured data.
- Clearly label assumptions when evidence is unavailable.
- Do not commit secrets, credentials, OAuth state, or machine-local configuration.
- Add or update tests with every change. If a test cannot be added, state the reason and what validation was run instead.
- When tests fail, identify the root cause before changing or dismissing the result, even if the failing case appears unrelated.
- When creating or amending Git commits, use Conventional Commits format (`type(scope): subject`).
- Split large or logically separate changes into multiple commits when that makes review or rollback clearer.
- Keep Git commit message lines wrapped at 72 characters when practical.
- For multi-line or multi-paragraph commit messages, preserve line breaks with separate `-m` flags or a commit message file instead of escaped `\n` in a single `-m` argument.
- Run the most relevant validation after setup changes and report any checks that were skipped.

## Candidate Chinese Writing Rules

Include this section only when the repository contains Chinese-facing content or the user requests
Chinese writing guidance:

- 使用自然、规范、符合中文语法习惯的表达。
- 避免照搬英文句式和明显的翻译腔。
- 不生造词语，不为了显得专业而使用少见、晦涩或不必要的表达。
- 避免不必要的互联网、商业和职场黑话，例如“深钻”“下挖”“口径”“抓手”“拉通”“对齐”“颗粒度”等；只有这些词在具体语境中确实准确、自然时才使用。
- 如果有常见、准确的中文表达，优先使用常见表达。
- 技术术语可以保留，但解释和叙述应尽量使用自然中文。

## Verification

- Every instruction maps to an explicit user request or inspected repository evidence.
- The file contains no placeholder headings or TODO-style template instructions.
- Generic rules inherited from a parent or global instruction file are not duplicated without a
  repository-specific reason.
- Real commands and paths replace generic descriptions whenever the repository provides them.
- The result is not a wholesale or near-wholesale copy of this guide.
- A second setup refresh would produce no diff.
