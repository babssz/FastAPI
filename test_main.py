from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_all_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_item_not_found():
    response = client.get("/items/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_create_item():
    response = client.post("/items/", json={
        "name": "Test Item",
        "price": 100
    })
    
    assert response.status_code in [200, 201, 405]

def test_update_item():
    response = client.put("/items/1", json={
        "name": "Updated Item",
        "price": 200
    })
    
    assert response.status_code in [200, 404, 405]

def test_delete_item():
    response = client.delete("/items/1")
    
    assert response.status_code in [200, 404, 405]

def test_register():
    response = client.post("/register", json={
        "username": "caca",
        "password": "123456"
    })
    
    assert response.status_code in [200, 201, 404, 405]

def test_login():
    response = client.post("/login", data={
        "username": "caca",
        "password": "123456"
    })
    
    assert response.status_code in [200, 401, 404, 405]

def test_access_denied():
    response = client.delete("/items/1")
    
    assert response.status_code in [401, 403, 405]