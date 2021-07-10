def test_index_route(app_client):
    resp = app_client.get("/")
    assert resp.status_code == 200
    assert "You visited this site 1 times" in resp.data.decode()


def test_ready_route(app_client):
    resp = app_client.get("/ready")
    assert resp.status_code == 200
    assert resp.data.decode() == "True"
