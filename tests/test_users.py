def test_get_users(client):
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) >= 20


def test_get_user_by_id(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json["user_id"] == 1
    assert "password_hash" not in response.json


def test_get_user_not_found(client):
    response = client.get("/users/99999")
    assert response.status_code == 404
    assert response.json["error"] == "User not found"


def test_add_user(client):
    response = client.post("/users/", json={
        "name": "Charlie Test",
        "phone": "+55 11 99999-3333",
        "street": "Rua dos Girassóis, 789",
        "city": "São Paulo",
        "neighborhood": "Vila Mariana",
        "zip_code": "04100-000",
        "state": "SP",
        "email": "charlie_test_unique@example.com",
        "password": "senhaSegura"
    })
    assert response.status_code == 201
    assert response.json["name"] == "Charlie Test"
    assert response.json["email"] == "charlie_test_unique@example.com"
    assert "password_hash" not in response.json


def test_add_user_missing_email(client):
    response = client.post("/users/", json={
        "name": "No Email",
        "password": "senha123"
    })
    assert response.status_code == 400
    assert response.json["error"] == "Email is required"


def test_add_user_missing_password(client):
    response = client.post("/users/", json={
        "name": "No Password",
        "email": "nopassword_unique@example.com"
    })
    assert response.status_code == 400
    assert response.json["error"] == "Password is required"


def test_update_user(client):
    response = client.put("/users/1", json={
        "name": "Alice Updated",
        "phone": "+55 11 99999-1112",
    })
    assert response.status_code == 200
    assert response.json["name"] == "Alice Updated"
    assert response.json["phone"] == "+55 11 99999-1112"


def test_update_user_not_found(client):
    response = client.put("/users/99999", json={"name": "Ghost"})
    assert response.status_code == 404


def test_delete_user(client):
    # Cria um usuário temporário para deletar
    add_response = client.post("/users/", json={
        "name": "Temp Delete User",
        "phone": "+55 11 99999-0000",
        "street": "Rua Exemplo, 123",
        "city": "São Paulo",
        "neighborhood": "Centro",
        "zip_code": "01000-000",
        "state": "SP",
        "email": "tempdelete_unique@example.com",
        "password": "tempSenha"
    })
    assert add_response.status_code == 201
    user_id = add_response.json["user_id"]

    # Deleta
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204

    # Confirma que foi deletado
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404
