# AGENTS.md Content Review

Use this review after the independent first draft, as described in the [setup workflow](../SKILL.md).
Questions identify possible omissions; add content only when current repository evidence or the
user's request establishes a need.

## Project Identity

- Does the draft say what this repository builds and which platforms or runtimes it supports when
  those constraints affect implementation?
- Did it capture real boundaries among domain logic, UI, tests, fixtures, generated code, and
  release assets that an agent could otherwise violate?
- Are all product names, target names, and paths current?

## Commands and Verification

- Did it capture relevant build, test, lint, format, run, release, or live-verification commands
  found in the repository or explicitly requested by the user?
- Does it say when each command applies rather than imposing every command on every edit?

- If this project needs tests with changes, does the draft say what to test and what validation to
  report when a test cannot practically be added?

- Does the project need an explicit instruction to identify the cause of every failing test before
  changing or dismissing it, including failures that appear unrelated?

- Does it require the most relevant validation and reporting of checks that were skipped?

## Working Boundaries and Evidence

- Does this repository need a local instruction to inspect Git status and existing project guidance
  before editing, or is that already inherited?

- Does it need a project-specific rule for keeping edits scoped and preserving unrelated changes?

- Does it need conclusions and recommendations supported by file references, command output, tests,
  experiments, source links, or measurements?

- Does it need assumptions to be labeled when evidence is unavailable?

- Is there a project-specific conflict that requires stating how current user instructions and
  current repository files interact with reusable skill guidance or older memory?

## Safety and Data Boundaries

- Does the project handle credentials, private data, hardware identifiers, generated files,
  external services, networks, or machine-local configuration?
- If so, are the actual files, APIs, data, and allowed operations described?
- Are generic safety statements omitted when higher-scope instructions already cover them?

- Does this repository need a concrete prohibition on committing secrets, credentials, OAuth state,
  or machine-local configuration?

## Agent-Specific Project Assets

- Does the repository actually contain project-owned skills, memory, checkpoints, hooks, or other
  agent assets, or did the user explicitly request them?

- Does this project have a reason to tell agents when a particular installed or project-owned skill
  should be used, beyond the skill's existing description?

- Could the repository be harmed by assuming Agent Toolbox supplies a multi-agent runtime that the
  project does not actually configure?

- Does it need a repository-specific boundary against vendoring or cloning reusable tooling?

- If project-owned skills exist, does the draft name their real directory and ownership boundary?

- If project memory or checkpoints were requested or already exist, does the draft keep them in the
  repository rather than reusable tooling?

- Does that durable context need an explicit provenance requirement?

- If the repository has no project-owned agent assets and the user did not request them, did setup
  avoid adding an Agent Toolbox or project-memory section merely because a reusable skill was used?
- If an Agent Toolbox-managed block is empty after generic content is removed, were its markers
  removed too?

## Git Delivery

- Does this repository need Conventional Commit subjects such as `type(scope): subject`, or is that
  rule already inherited?

- Does it need logically independent changes split when that improves review or rollback?

- Does it need commit-message lines wrapped at 72 characters when practical?

- Does it need multi-paragraph commit messages written with separate `-m` flags or a message file
  rather than escaped `\n` text?

## Language and Domain Terms

- Does the repository contain user-facing language that needs a project-specific style or
  localization rule?
- Are established domain terms, spelling, and capitalization visible in current source or docs?
- Does the draft describe those concrete conventions instead of importing a general writing guide?

When Chinese-facing content is present or Chinese guidance was requested, review these earlier
writing expectations without automatically copying them into the project file:

- Does the draft call for natural, standard Chinese that follows common Chinese grammar?

- Does it avoid copied English sentence patterns and obvious translationese?

- Does it avoid invented, obscure, or needlessly ornate wording?

- Does it avoid unnecessary internet, business, or workplace jargon such as “深钻”“下挖”“口径”
  “抓手”“拉通”“对齐”和“颗粒度” when those terms are not genuinely natural and precise?

- Does it prefer common, accurate Chinese when one is available?

- Does it retain accurate technical terms while keeping explanations and narration natural?

## Final Audit

- Can every sentence be traced to an explicit user request or a current repository file?
- Are inherited rules, generic workflow advice, placeholder headings, and template-shaped sections
  absent?
- Would a second setup or refresh run produce no diff?
