---
name: agent-toolbox
description: Use when the user asks for Agent Toolbox, an agent team, specialist agents, coordinated planning/research/design/implementation/review, or the Agent Toolbox Learning Coach.
---

# Agent Toolbox

Use this skill to load the reusable Agent Toolbox team and route work through the smallest useful
set of specialist profiles.

## Required Context Load

1. Read `../../team.yaml` first to understand the roster, workflows, memory layout, and file paths.
2. Choose one workflow:
   - Use `../../workflows/default-cycle.md` for delivery, implementation, research, planning, and review tasks.
   - Use `../../workflows/learning-cycle.md` when the user wants to learn a topic or asks for the Learning Coach.
3. Read only the agent profiles needed for the task from `../../agents/`.
4. Read relevant reusable memory templates from `../../memory/` only when they help the current task.

## Routing Guidance

- Use Lead Orchestrator when the task spans multiple specialists or needs explicit coordination.
- Use Product Strategist for scope, requirements, user needs, and acceptance criteria.
- Use Research Analyst when current, external, or source-backed information is needed.
- Use Learning Coach for teaching, first-principles explanations, practice, and durable understanding.
- Use Solution Architect for technical design, integration decisions, and risk tradeoffs.
- Use Implementation Engineer for code, config, docs, tests, and local verification.
- Use QA Reviewer for review, edge cases, regressions, missing tests, and release readiness.

## Memory Boundary

Treat bundled memory as reusable context, not canonical truth. Current user instructions, current
repository files, and fresh source-backed facts take precedence. Keep project-specific checkpoints,
local preferences, secrets, credentials, and private notes in the project using the plugin, not in
Agent Toolbox.

## Commit Rules

When creating commits while using Agent Toolbox, use Conventional Commits. Wrap every commit message
line, including the subject and body, at 120 characters or less. Do not embed literal `\n` escape
sequences in commit message arguments; use separate `-m` flags for subject and body paragraphs.

## Delivery

When responding, summarize the selected workflow, the specialists used, the concrete result, and
any verification performed. Mention memory update candidates only when the information is durable
and belongs in the user's project or explicit memory system.
