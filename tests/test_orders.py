def test_get_orders(client):
    response = client.get("/orders/")
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) >= 10


def test_add_order(client):
    response = client.post("/orders/", json={"user_id": 1, "item": "Tablet"})
    assert response.status_code == 201
    assert response.json["item"] == "Tablet"
    assert response.json["user_id"] == 1
