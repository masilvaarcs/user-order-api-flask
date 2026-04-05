import sys
import os
import pytest

# Adiciona src/ ao path para imports funcionarem como na execução real
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import app as flask_app


@pytest.fixture
def app():
    flask_app.config["TESTING"] = True
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
