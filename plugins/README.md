# Plugins

Installable Codex plugin bundles live here.

`agent-toolbox/` is the primary package exposed by the root marketplace at
`.agents/plugins/marketplace.json`.

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
