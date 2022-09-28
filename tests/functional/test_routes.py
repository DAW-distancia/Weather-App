from weather_app.models import City


def test_index_route_GET(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"How\'s the weather today?" in response.data


def test_index_route_with_actual_city_POST(client):
    city_data = {"city": "Manhattan"}
    response = client.post("/", data=city_data)
    assert response.status_code == 302
    assert len(City.query.all()) == 1
    assert str(City.query.all()[0]) == "manhattan"


def test_index_route_with_fake_city_POST(client):
    city_data = {"city": "Imaginaryland"}
    response = client.post("/", data=city_data)
    assert response.status_code == 302
    assert len(City.query.all()) == 1


def test_delete_city_route(client):
    response = client.get("/delete/manhattan")
    assert response.status_code == 302
    assert len(City.query.all()) == 0
