---
name: audit-agent-assets
description: Audit and modernize a repository's Markdown documentation and agent-facing instruction assets for concise, reliable, context-efficient use. Use when the user asks to review AGENTS.md, CLAUDE.md, skills, rules, prompts, memory guidance, MCP documentation, or a full documentation corpus for verbosity, duplication, conflicts, poor routing, outdated model assumptions, capability upgrades, or reconstruction opportunities. Produce evidence-backed advice without rewriting files unless the user asks for implementation.
---

# Audit Agent Assets

Review the corpus as an instruction system, not merely as prose. Optimize for reliable task
performance per unit of context, not for the shortest possible text.

## Boundaries

- Treat the audit as read-only unless the user explicitly asks to apply the recommendations.
- Preserve user intent, authority boundaries, safety constraints, exact commands, and essential
  domain context. Compactness is not a reason to remove decision-changing information.
- Distinguish human documentation, always-loaded instructions, skill-selection metadata,
  conditionally loaded references, prompts, memory guidance, and structured agent configuration.
  They have different audiences and context costs.
- Do not compress a human-facing README into prompt shorthand or penalize generated, vendored, or
  schema-driven assets for necessary structure. Identify them separately.
- Do not assume that a newer or larger model makes safety boundaries, project facts, deterministic
  checks, or explicit acceptance criteria obsolete. Modernize only where current capabilities make
  the old instruction or scaffold unnecessary or counterproductive.

## Workflow

1. Establish scope and coverage.
   - Inspect repository status and applicable instructions before reading the corpus.
   - Inventory Markdown and agent-specific assets, including nested instruction files, skill
     entrypoints and metadata, prompts, rules and policies, memory and retrieval guidance, tool or
     MCP descriptions and schemas, manifests, hooks, workflows, examples, and agent evaluations
     when present.
   - Classify each item by audience, owner, authority, and loading behavior: always loaded,
     selected by metadata, loaded through a reference, or consulted only by a human.
   - Read every in-scope asset when practical. For a corpus too large to inspect completely, define
     a defensible sample, report exactly what was and was not read, and do not claim full coverage.

2. Evaluate the information architecture.
   - **Purpose and placement:** Does the content change an agent's decisions, and is it stored at
     the narrowest correct scope and in the right asset type?
   - **Routing and discovery:** Are names, descriptions, links, and entrypoints precise enough to
     load the right material without loading unrelated detail?
   - **Signal density:** Identify generic advice, repeated explanations, redundant examples,
     ceremonial headings, and background that does not affect action.
   - **Actionability:** Check commands, paths, prerequisites, permissions, stop conditions,
     validation, ownership, and expected outcomes. Concise but underspecified guidance is not
     efficient.
   - **Consistency:** Find contradictory instructions, semantic drift between copies, stale facts,
     broken references, unclear precedence, and inconsistent terminology or modality.
   - **Progressive disclosure:** Keep frequent, cross-cutting decisions near the entrypoint; move
     substantial conditional detail to discoverable references; remove indirection that saves no
     context or obscures required steps.
   - **Agent readability:** Prefer explicit scope and unambiguous verbs. Distinguish requirements
     from recommendations, and pair important prohibitions with the permitted alternative or stop
     condition when needed.

3. Assess capability fit and upgrade value.
   - Identify the target clients, model classes, tools, context-loading behavior, and supported
     modalities from current configuration or authoritative documentation when practical. If they
     are unknown, state capability-dependent recommendations conditionally instead of guessing.
   - Look for scaffolding built around older limitations: rigid task decomposition, prescribed
     prose or section templates, repeated reminders, excessive examples, manual tool inventories,
     hard-coded model capabilities, forced reasoning rituals, and context copied eagerly instead
     of retrieved when needed.
   - Check whether stronger synthesis, planning, tool use, structured output, retrieval, or
     multimodal input can replace that scaffolding with outcomes, invariants, schemas, routing
     metadata, or validation. Recommend only capabilities supported by the target runtime.
   - Check whether the client now provides a native skill, tool, policy, hook, retrieval, or
     orchestration mechanism that makes a custom asset redundant or gives it a better enforcement
     surface. Verify the native behavior before recommending migration.
   - Prefer capability-based requirements over model-name-specific advice when practical. Preserve
     compatibility with smaller or older supported models; propose variants only when one asset
     cannot serve the supported range effectively.
   - Record the model and runtime capability baseline used for the audit and name concrete
     re-audit triggers, such as a client capability change, new tool interface, or evaluation
     regression. Avoid claims based only on "latest" or an assumed release cadence.
   - Treat modernization as a performance hypothesis. Define a representative forward test and
     compare task success, instruction adherence, context use, latency or tool churn, and failure
     modes before claiming that a reconstruction performs better.

4. Support findings with evidence.
   - Cite exact files and tight line ranges. Trace duplicated or conflicting guidance to every
     affected source rather than asserting that it exists.
   - Validate local links and parse structured frontmatter or configuration when relevant.
   - Use line, word, or token estimates only as supporting evidence. Label estimates and do not use
     document length as a proxy for quality.
   - Separate confirmed defects from editorial judgment and unknown loading behavior. Do not assume
     every Markdown file enters the model context.

5. Design the reconstruction.
   - For each proposed change, state the current problem, target location, operation (`keep`,
     `rewrite`, `move`, `merge`, `split`, or `delete`), constraints that must survive, expected
     benefit, and migration risk.
   - Propose a target map of canonical sources, entrypoints, and conditional references. Prefer one
     authoritative statement with links over synchronized copies unless the runtime requires
     duplication.
   - Include small representative rewrites only when they clarify the recommendation. Do not
     rewrite the entire corpus inside the audit.
   - Prioritize contradictions or unsafe ambiguity first, likely task failures second, recurring
     context waste or drift third, and cosmetic polish last.

## Delivery

Lead with the overall verdict and highest-leverage reconstruction. Then provide:

- a coverage table listing the reviewed asset groups, audiences, and loading behavior;
- prioritized findings with evidence, agent impact, and a concrete recommendation;
- a capability-upgrade matrix classifying asset groups as current, modernize, replace or retire,
  or conditional, with the capability baseline used for that judgment;
- a reconstruction map showing what stays, moves, merges, splits, modernizes, or disappears;
- constraints that must be preserved, uncertainties, exclusions, and skipped validation.

Group one systemic finding across all affected files instead of repeating it per file. Avoid a
false-precision aggregate score unless the user requests a comparison. If the corpus is already
compact and effective, say so and recommend only changes whose benefit exceeds their churn.
