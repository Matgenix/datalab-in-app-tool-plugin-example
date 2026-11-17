# Hello in-app

Hello in-app is a minimal example tool that runs below datalab's normal
navigation. It demonstrates the frontend SDK without adding custom data routes.

## Use the tool

1. Sign in to datalab and click **Tools**.
2. Choose **Hello in-app**.
3. Confirm that the page greets you and shows how many samples your account can
   access.

The number is permission-filtered by datalab. If the tool is absent from the
complete Tools catalog, ask the deployment administrator whether the plugin is
installed and enabled. If its page cannot load the module, the administrator
should verify that the compiled frontend bundle was included in the installed
release.

Deployment administrators should follow the repository's
[installation guide](https://github.com/Matgenix/datalab-in-app-tool-plugin-example/blob/main/INSTALL.md).
Developers can reproduce the implementation with datalab's
[in-app tool tutorial](https://docs.datalab-org.io/en/latest/plugin-development/in-app-tool-plugin/).
