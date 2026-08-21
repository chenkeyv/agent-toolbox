# Agent Project Instructions

Use this as a starting point, then tailor it to the target project.

```md
# Agent Project Instructions

<!-- agent-toolbox:start -->
## Agent Toolbox Setup

- This repository uses the installed Agent Toolbox Agent Plugin or project-owned skills in the active client's supported location.
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
- Keep repository-specific skills in the active client's project-owned skills directory.
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

## 中文表达

- 使用自然、规范、符合中文语法习惯的表达。
- 避免照搬英文句式和明显的翻译腔。
- 不生造词语，不为了显得专业而使用少见、晦涩或不必要的表达。
- 避免不必要的互联网、商业和职场黑话，例如“深钻”“下挖”“口径”“抓手”“拉通”“对齐”“颗粒度”等；只有这些词在具体语境中确实准确、自然时才使用。
- 如果有常见、准确的中文表达，优先使用常见表达。
- 技术术语可以保留，但解释和叙述应尽量使用自然中文。
<!-- agent-toolbox:end -->

## Project-Specific Rules

- Add repository-specific build, test, lint, release, and ownership rules here.
```
