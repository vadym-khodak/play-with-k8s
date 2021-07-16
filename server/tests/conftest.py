from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def app_client():
    from main import app

    client = TestClient(app)
    yield client
