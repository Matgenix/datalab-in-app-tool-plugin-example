# datalab Hello In-App Tool

Minimal *in-app tool* plugin. It renders below the normal datalab navigation,
uses the frontend SDK, and prints one datalab-backed message. datalab
automatically protects its *provider blueprint*, while the SDK uses the current
*browser session* for normal *permission-aware API* requests.

## Build the frontend bundle

```shell
cd frontend
yarn install
yarn build
```

## Local installation

Add the package to the root `plugins.toml`:

```toml
dependencies = ["datalab-hello-in-app-tool"]

[tool.uv.sources]
datalab-hello-in-app-tool = { path = "dev-repos/datalab-in-app-tool-plugin-example", editable = true }
```

Then install datalab with plugins:

```shell
cd pydatalab
uv run invoke dev.install
```

See the
[in-app Tool plugin tutorial](https://docs.datalab-org.io/plugin-development/in-app-tool-plugin/)
for a step-by-step explanation.
