# Installation

This plugin runs trusted Python in the datalab API and trusted JavaScript in
signed-in users' pages. Review the selected release, Python and frontend
dependencies, lockfile, and compiled bundle before installation or upgrade.

## Install in datalab

Add the plugin to the datalab checkout's root `plugins.toml`, preserving any
existing entries:

```toml
dependencies = ["datalab-hello-in-app-tool"]

[tool.uv.sources]
datalab-hello-in-app-tool = { git = "https://github.com/Matgenix/datalab-in-app-tool-plugin-example.git", rev = "<reviewed-tag-or-commit>" }
```

Install the configured plugins:

```shell
cd pydatalab
uv run invoke dev.install
```

Restart a native API, or rebuild and recreate the Docker images. Sign in as a
normal user, open **Tools**, and confirm that **Hello in-app** displays the user
and accessible sample count.

Use datalab's
[plugin operations guide](https://docs.datalab-org.io/en/latest/plugins/#installing-and-maintaining-plugins)
for Docker behavior, upgrades, rollback, removal, and tool ordering or disabling.

## Development setup

```shell
git clone https://github.com/Matgenix/datalab-in-app-tool-plugin-example.git
cd datalab-in-app-tool-plugin-example
uv sync --locked --all-extras --dev
uv run pytest
uv run pre-commit run --all-files
```

After changing the frontend, rebuild its committed bundle:

```shell
cd frontend
corepack yarn install --frozen-lockfile
corepack yarn build
cd ..
```

Commit `frontend/yarn.lock` and
`src/datalab_hello_in_app_tool/static/frontend/tool.js`.

For integration testing, change the Git source above to an editable path to
this checkout, rerun `uv run invoke dev.install`, and restart datalab.
