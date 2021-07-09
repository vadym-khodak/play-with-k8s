import pytest


@pytest.fixture
def app_client():
    from app import app

    app.testing = True
    with app.app_context():
        with app.test_client() as c:
            yield c
