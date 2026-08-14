# Implementação demonstrativa — três práticas de código seguro

API FastAPI de um delivery, com dados em memória, criada para demonstração acadêmica. O fluxo cobre RBAC e menor privilégio, proteção contra tampering de pedidos e consumo seguro da API externa de pagamentos com timeout e circuit breaker (`CLOSED`, `OPEN` e `HALF_OPEN`).

## Execução

No PowerShell, em `implementacao`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Terminal 1 — serviço simulado de pagamentos:

```powershell
uvicorn payment_api.main:app --port 8001
```

Terminal 2 — backend:

```powershell
$env:DEMO_MODE="true"
uvicorn app.main:app --reload --port 8000
```

Acesse `http://127.0.0.1:8000`. Cadastre um cliente, faça login e abra `/pedido`. O administrador é criado internamente: `admin@delivery.example` / `Admin#2026`.

## Demonstração do circuit breaker

Com `DEMO_MODE=true`, um administrador pode usar os endpoints de simulação:

```powershell
$h=@{Authorization="Bearer SEU_TOKEN_ADMIN";"Content-Type"="application/json"}
Invoke-RestMethod http://127.0.0.1:8000/api/v1/admin/simulation/config -Method Post -Headers $h -Body '{"failure":true}'
Invoke-RestMethod http://127.0.0.1:8000/api/v1/admin/simulation/status -Headers $h
Invoke-RestMethod http://127.0.0.1:8000/api/v1/admin/simulation/reset -Method Post -Headers $h
```

Falhas consecutivas abrem o circuito; chamadas seguintes são bloqueadas sem alcançar o gateway. Após o período de recuperação, a próxima chamada é uma tentativa `HALF_OPEN`.

## Testes

```powershell
python -m pytest -q
```

Os testes não dependem de um gateway real: o cliente de pagamento é mockado nos testes de pedido e o circuito é testado com relógio controlado.
