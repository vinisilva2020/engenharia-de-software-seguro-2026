from app.main import app
from app.core.security import Role
from app.repositories.users import create_user, authenticate
from app.services import orders
from app.services.payment_client import PaymentClient
from fastapi.testclient import TestClient

client = TestClient(app)

def auth_client():
    email = f"cliente.{len(orders.ORDERS) + 2}@example.com"
    user = create_user("Cliente teste", email, "Senha#123", Role.CLIENTE)
    token = authenticate(user.email, "Senha#123")
    return {"Authorization": f"Bearer {token}"}

def test_order_uses_server_price_and_accepts_valid_item(monkeypatch):
    monkeypatch.setattr(PaymentClient, "create_payment", lambda self, order_id, amount: {"id": "pay-test"})
    response = client.post("/api/v1/orders", headers=auth_client(), json={"establishment_id": 1, "items": [{"product_id": 1, "quantity": 2}]})
    assert response.status_code == 201
    assert response.json()["total"] == 65.80

def test_order_rejects_tampered_product_from_other_establishment(monkeypatch):
    monkeypatch.setattr(PaymentClient, "create_payment", lambda *args: {"id": "unused"})
    response = client.post("/api/v1/orders", headers=auth_client(), json={"establishment_id": 1, "items": [{"product_id": 4, "quantity": 1}]})
    assert response.status_code == 400
