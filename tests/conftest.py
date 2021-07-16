import pytest


@pytest.fixture
def app_client():
    from flask_server.app import app

    app.testing = True
    with app.app_context():
        with app.test_client() as c:
            yield c
