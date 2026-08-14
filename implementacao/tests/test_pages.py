from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_order_page_is_available():
    response = client.get("/pedido")
    assert response.status_code == 200
    assert 'id="finish"' in response.text

def test_customer_panel_contains_order_navigation():
    response = client.get("/painel/cliente")
    assert response.status_code == 200
    assert 'id="novo-pedido"' in response.text
    assert 'window.location.assign("/pedido")' in response.text
