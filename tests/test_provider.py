from datalab_hello_in_app_tool import __version__
from datalab_hello_in_app_tool.provider import (
    HelloInAppToolProvider,
)


def test_provider_metadata():
    provider = HelloInAppToolProvider()

    assert provider.id == "hello-in-app"
    assert provider.metadata.version == __version__
    assert provider.metadata.ui.kind == "in_app"
