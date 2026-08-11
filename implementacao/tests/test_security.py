from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_cadastro_login_me_sem_expor_segredos():
    assert client.post('/api/v1/auth/register/clientes', json={'name':'Ana','email':'ana@example.com','password':'SenhaSegura#2026'}).status_code == 201
    login = client.post('/api/v1/auth/login', json={'email':'ana@example.com','password':'SenhaSegura#2026'})
    me = client.get('/api/v1/me', headers={'Authorization': f"Bearer {login.json()['access_token']}"})
    assert me.status_code == 200
    assert 'password_hash' not in me.text and 'SenhaSegura' not in me.text


def test_cliente_nao_acessa_area_admin():
    login = client.post('/api/v1/auth/login', json={'email':'ana@example.com','password':'SenhaSegura#2026'})
    response = client.get('/api/v1/admin/usuarios', headers={'Authorization': f"Bearer {login.json()['access_token']}"})
    assert response.status_code == 403


def test_sem_token_e_token_revogado_nao_acessam_informacoes():
    assert client.get('/api/v1/me').status_code == 401
    login = client.post('/api/v1/auth/login', json={'email':'admin@delivery.example','password':'Admin#2026'})
    headers = {'Authorization': f"Bearer {login.json()['access_token']}"}
    assert client.post('/api/v1/auth/logout', headers=headers).status_code == 204
    assert client.get('/api/v1/me', headers=headers).status_code == 401


def test_paineis_existentes_sao_apenas_apresentacao_e_api_valida_rbac():
    assert client.get('/painel/cliente').status_code == 200
    login = client.post('/api/v1/auth/login', json={'email':'admin@delivery.example','password':'Admin#2026'})
    headers = {'Authorization': f"Bearer {login.json()['access_token']}"}
    assert client.get('/api/v1/areas/cliente', headers=headers).status_code == 403