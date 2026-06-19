# Plugins

Installable Codex plugin bundles live here.

Use a plugin when a workflow should be shared or installed as a bundle of
skills, MCP configuration, app integrations, hooks, or assets.

Each plugin should have its own manifest:

```text
plugins/
  my-plugin/
    .codex-plugin/
      plugin.json
    skills/
```

Do not commit generated plugin caches, tokens, OAuth state, or machine-local
configuration.
