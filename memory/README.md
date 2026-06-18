# Memory

AgentTeam memory is explicit, file-based, and reviewable. Agents may use it as context, but
must not treat it as more authoritative than the current user request, current project files,
or fresh source-backed facts.

## Memory Stores

| Store | File | Purpose |
| --- | --- | --- |
| Project memory | [project.md](project.md) | Stable repo conventions, architecture decisions, and workflow norms. |
| User preferences | [user-preferences.md](user-preferences.md) | Explicit user preferences that should shape future work. |
| Research memory | [research.md](research.md) | Source-backed facts, comparisons, and external references. |
| Agent memory | [agents/](agents/) | Role-specific operating notes and lessons learned. |
| Schema | [schema.yaml](schema.yaml) | Required fields and validation guidance for structured memory entries. |

## Read Rules

1. Read only memory that is relevant to the task.
2. Prefer current instructions, current files, and fresh sources over memory.
3. Check `confidence`, `updated_at`, and `expires_at` before relying on an entry.
4. Treat unsourced or stale memory as a hint, not evidence.
5. Surface contradictions instead of silently choosing one version.

## Write Rules

1. Write memory only when it is likely to be useful beyond the current task.
2. Include `id`, `scope`, `owner`, `content`, `source`, `confidence`, and `updated_at`.
3. Prefer updating an existing entry over creating a duplicate.
4. Add `expires_at` for facts that can change, such as APIs, pricing, policies, dependencies, or market data.
5. Do not store secrets, credentials, tokens, private personal details, or unverified sensitive claims.

## Entry Template

```yaml
- id: mem-000
  scope: project
  owner: orchestrator
  content: "Short reusable memory written as a concrete fact or preference."
  source: "Where this came from."
  confidence: medium
  updated_at: 2026-06-18
  expires_at: null
  tags:
    - example
```

## Memory Scopes

- `working`: Useful only during the current task. Usually do not commit it.
- `project`: Stable knowledge about this repository or team.
- `agent`: Role-specific operating memory.
- `research`: Source-backed external facts.
- `user-preference`: Explicit preferences from the user.

