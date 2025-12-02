from fastapi.testclient import TestClient
from app.main import app
from app.schemas.order import OrderCreate, OrderRead
from app.services.order_service import create_order, get_order

client = TestClient(app)

def test_create_order():
    order_data = {
        "customer_id": 1,
        "product_id": 2,
        "quantity": 3,
        "status": "pending"
    }
    response = client.post("/api/v1/orders/", json=order_data)
    assert response.status_code == 201
    order = response.json()
    assert order["customer_id"] == order_data["customer_id"]
    assert order["product_id"] == order_data["product_id"]
    assert order["quantity"] == order_data["quantity"]
    assert order["status"] == order_data["status"]

def test_get_order():
    response = client.get("/api/v1/orders/1")
    assert response.status_code == 200
    order = response.json()
    assert order["id"] == 1
    assert "customer_id" in order
    assert "product_id" in order
    assert "quantity" in order
    assert "status" in order

def test_get_nonexistent_order():
    response = client.get("/api/v1/orders/999")
    assert response.status_code == 404