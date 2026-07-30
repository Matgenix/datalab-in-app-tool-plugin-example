# Hello in-app

A minimal in-app Hello World tool for datalab

This package provides a trusted datalab
in-app tool
through the `pydatalab.tools` entry-point group.

It demonstrates the in-app frontend SDK by showing the current user and their
permission-filtered sample count.

See the
[installation guide](https://github.com/Matgenix/datalab-in-app-tool-plugin-example/blob/main/INSTALL.md)
and the
[in-app tool plugin tutorial](https://docs.datalab-org.io/plugin-development/in-app-tool-plugin/).

## Trust

Tool plugins execute trusted Python code in the datalab API process.

This plugin also loads trusted JavaScript in the signed-in datalab application.

Deployment administrators must review source code, dependencies, compiled
assets, maintainers, and release provenance before installation or upgrade.
