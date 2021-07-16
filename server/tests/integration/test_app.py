def test_index_route(app_client):
    resp = app_client.get("/", headers={'Access-Control-Allow-Origin': "true", "user": "12345"})
    assert resp.status_code == 200
    print(resp.json())

    for key in ["counter", "hostName", "userId"]:
        assert key in resp.json()

    assert resp.json()["userId"] == "12345"


def test_ready_route(app_client):
    resp = app_client.get("/ready", headers={'Access-Control-Allow-Origin': "true"})
    print(resp.json())
    assert resp.status_code == 200
    assert resp.json()["is_redis_ready"]
