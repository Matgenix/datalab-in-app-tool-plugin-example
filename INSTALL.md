# Installation and development

Install [uv](https://docs.astral.sh/uv/) and clone the repository:

```shell
git clone https://github.com/Matgenix/datalab-in-app-tool-plugin-example.git
cd datalab-in-app-tool-plugin-example
uv sync --locked --all-extras --dev
uv run pre-commit install
```


Build the in-app frontend:

```shell
cd frontend
corepack yarn install --frozen-lockfile
corepack yarn build
cd ..
```

Commit `frontend/yarn.lock` and
`src/datalab_hello_in_app_tool/static/frontend/tool.js`.


## Install in a datalab checkout

Add the plugin to the datalab checkout's root `plugins.toml`:

```toml
dependencies = ["datalab-hello-in-app-tool"]

[tool.uv.sources]
datalab-hello-in-app-tool = { path = "dev-repos/datalab-in-app-tool-plugin-example", editable = true }
```

Preserve existing dependencies and source entries when merging this
configuration. Then install the configured plugins:

```shell
cd pydatalab
uv run invoke dev.install
```

Restart the datalab API after installation so it discovers the
`pydatalab.tools` entry point.
