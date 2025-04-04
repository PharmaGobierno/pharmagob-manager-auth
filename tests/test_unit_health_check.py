from httpx import Response


def test_health_check(client):
    response: Response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "200, OK"
