from flask import Flask

from datalab_hello_in_app_tool import __version__
from datalab_hello_in_app_tool.provider import (
    TOOL_BLUEPRINT,
    HelloInAppToolProvider,
)


def test_provider_metadata():
    provider = HelloInAppToolProvider()

    assert provider.id == "hello-in-app"
    assert provider.metadata.version == __version__
    assert provider.metadata.ui.kind == "in_app"


def test_frontend_bundle_route_sets_safe_headers():
    app = Flask(__name__)
    app.register_blueprint(TOOL_BLUEPRINT, url_prefix="/tool")

    response = app.test_client().get("/tool/frontend/tool.js")

    assert response.status_code == 200
    assert response.mimetype == "text/javascript"
    assert response.headers["Cache-Control"] == "no-cache"
    assert response.headers["X-Content-Type-Options"] == "nosniff"
