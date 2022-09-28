def test_index_route_GET(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"How\'s the weather today?" in response.data
