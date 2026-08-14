"""API demonstrativa do fluxo seguro de cadastro, login e RBAC."""

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.core.security import Role, User, current_user, require_roles
from app.repositories.users import authenticate, create_user, revoke
from app.schemas import Credentials, OrderRequest, PublicUser, Registration
from pathlib import Path
from app.services.orders import create_order, user_orders
from app.services.catalog import list_establishments, list_menu
from app.services.circuit_breaker import circuit_breaker
from payment_api.simulation import state as payment_simulation
import os

app = FastAPI(title="Delivery Seguro API", version="1.0.0")
DEMO_MODE = os.getenv("DEMO_MODE", "false").lower() == "true"
app.mount(
    "/static",
    StaticFiles(directory=str(Path(__file__).parent / "static")),
    name="static",
)
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


def public(user: User) -> PublicUser:
    """Converte entidade interna em DTO allowlist, evitando exposição acidental."""
    return PublicUser(id=user.id, name=user.name, email=user.email, role=user.role)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/v1/auth/register/{role}", response_model=PublicUser, status_code=201)
def register(role: str, data: Registration):
    """Cadastro público; qualquer papel não permitido é rejeitado."""
    try:
        selected = {
            "clientes": Role.CLIENTE,
            "entregadores": Role.ENTREGADOR,
            "estabelecimentos": Role.ESTABELECIMENTO,
        }[role]
    except KeyError as exc:
        raise HTTPException(403, "Papel não pode ser criado publicamente") from exc
    try:
        return public(create_user(data.name, data.email, data.password, selected))
    except ValueError as exc:
        raise HTTPException(409, str(exc)) from exc


@app.post("/api/v1/auth/login")
def login(data: Credentials):
    """Retorna somente token e tipo; detalhes de autenticação não vazam."""
    token = authenticate(data.email, data.password)
    if not token:
        raise HTTPException(401, "E-mail ou senha inválidos")
    return {"access_token": token, "token_type": "bearer"}


@app.post("/api/v1/auth/logout", status_code=204)
def logout(request: Request, _user: User = Depends(current_user)):
    token = request.headers["authorization"].split(" ", 1)[1]
    revoke(token)


@app.get("/api/v1/me", response_model=PublicUser)
def me(user: User = Depends(current_user)):
    """Retorna somente o perfil mínimo do usuário autenticado."""
    return public(user)


@app.get("/api/v1/areas/{role}")
def area(role: str, user: User = Depends(current_user)):
    """A rota valida o papel no servidor; não confia no valor enviado pelo cliente."""
    if role != user.role.value:
        raise HTTPException(403, "Permissão insuficiente")
    return {"area": user.role.value, "message": f"Olá, {user.name}"}


@app.get(
    "/api/v1/admin/usuarios", dependencies=[Depends(require_roles(Role.ADMINISTRADOR))]
)
def admin_users():
    """Endpoint admin sem senha/hash: ainda assim restringido por RBAC."""
    from app.repositories.users import USERS

    return [public(user) for user in USERS.values()]


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="home.html")


@app.get("/cadastro", response_class=HTMLResponse)
def registration_page(request: Request):
    return templates.TemplateResponse(request=request, name="cadastro.html")


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


@app.get("/painel/{role}", response_class=HTMLResponse)
def dashboard_page(request: Request, role: str):
    """Entrega apenas a casca visual; a API ainda valida o papel no servidor."""
    allowed = {"cliente", "entregador", "estabelecimento", "administrador"}
    if role not in allowed:
        raise HTTPException(404, "Painel não encontrado")
    return templates.TemplateResponse(request=request, name=f"painel_{role}.html")


@app.post("/api/v1/orders", status_code=201, tags=["orders"])
def create_order_endpoint(data: OrderRequest, user: User = Depends(require_roles(Role.CLIENTE))):
    return create_order(user.id, data.establishment_id, [item.model_dump() for item in data.items])


@app.get("/api/v1/orders", tags=["orders"])
def list_orders_endpoint(user: User = Depends(require_roles(Role.CLIENTE))):
    return user_orders(user.id)

@app.get("/api/v1/establishments", tags=["catalog"])
def establishments_endpoint(user: User = Depends(current_user)):
    return list_establishments()

@app.get("/api/v1/establishments/{establishment_id}/menu", tags=["catalog"])
def menu_endpoint(establishment_id: int, user: User = Depends(current_user)):
    return list_menu(establishment_id)

@app.get("/pedido", response_class=HTMLResponse)
def order_page(request: Request):
    return templates.TemplateResponse(request=request, name="pedido.html")


def simulation_snapshot():
    return {"payment_api": payment_simulation.__dict__, "circuit_breaker": circuit_breaker.snapshot()}


@app.get("/api/v1/admin/simulation/status", tags=["simulation"])
def simulation_status(user: User = Depends(require_roles(Role.ADMINISTRADOR))):
    if not DEMO_MODE: raise HTTPException(404, "Modo demonstração desativado")
    return simulation_snapshot()


@app.post("/api/v1/admin/simulation/config", tags=["simulation"])
def simulation_config(data: dict, user: User = Depends(require_roles(Role.ADMINISTRADOR))):
    if not DEMO_MODE: raise HTTPException(404, "Modo demonstração desativado")
    for key in ("failure", "rejection", "latency"):
        if key in data: setattr(payment_simulation, key, data[key])
    return simulation_snapshot()


@app.post("/api/v1/admin/simulation/reset", tags=["simulation"])
def simulation_reset(user: User = Depends(require_roles(Role.ADMINISTRADOR))):
    if not DEMO_MODE: raise HTTPException(404, "Modo demonstração desativado")
    payment_simulation.failure = payment_simulation.rejection = False; payment_simulation.latency = 0
    circuit_breaker.reset(); return simulation_snapshot()

@app.get("/api/v1/demo/simulation/status", tags=["simulation"])
def demo_simulation_status(user: User = Depends(require_roles(Role.CLIENTE))):
    if not DEMO_MODE: raise HTTPException(404, "Modo demonstração desativado")
    return simulation_snapshot()

@app.post("/api/v1/demo/simulation/config", tags=["simulation"])
def demo_simulation_config(data: dict, user: User = Depends(require_roles(Role.CLIENTE))):
    if not DEMO_MODE: raise HTTPException(404, "Modo demonstração desativado")
    payment_simulation.failure = bool(data.get("failure", False))
    payment_simulation.rejection = bool(data.get("rejection", False))
    payment_simulation.latency = max(0.0, min(float(data.get("latency", 0)), 10.0))
    return simulation_snapshot()

@app.post("/api/v1/demo/simulation/reset", tags=["simulation"])
def demo_simulation_reset(user: User = Depends(require_roles(Role.CLIENTE))):
    if not DEMO_MODE: raise HTTPException(404, "Modo demonstração desativado")
    payment_simulation.failure = payment_simulation.rejection = False
    payment_simulation.latency = 0
    circuit_breaker.reset()
    return simulation_snapshot()
