# Skills

Reusable Agent Skills live here.

Use one directory per skill:

```text
skills/
  example-skill/
    SKILL.md
    references/
    scripts/
```

Keep skill descriptions specific enough that compatible clients can choose the skill
implicitly when a task matches it. Put large references and helper scripts next
to the skill instead of expanding `SKILL.md` unnecessarily.

## Included Skills

| Skill | Purpose |
| --- | --- |
| `audit-agent-assets` | Audit and modernize agent-facing assets for context efficiency and current model capabilities. |
| `prevent-repeat` | Investigate missed behavior and apply durable prevention. |
| `rename-master-to-main` | Migrate `master` to `main` with verified history preservation and guarded cleanup. |
| `setup-agent-project` | Discover client guidance and refresh evidence-driven project instructions idempotently. |
