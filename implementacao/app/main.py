"""API demonstrativa do fluxo seguro de cadastro, login e RBAC."""

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.core.security import Role, User, current_user, require_roles
from app.repositories.users import authenticate, create_user, revoke
from app.schemas import Credentials, PublicUser, Registration
from pathlib import Path

app = FastAPI(title="Delivery Seguro API", version="1.0.0")
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
