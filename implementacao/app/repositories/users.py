"""Persistência didática em memória; só para fazer a demonstração"""

from app.core.security import Role, User, hash_password, verify_password
import secrets

# O administrador é criado internamente; não existe endpoint público para esse papel.
USERS = {
    1: User(
        1,
        "Administrador",
        "admin@delivery.example",
        Role.ADMINISTRADOR,
        hash_password("Admin#2026"),
    )
}
TOKENS: dict[str, int] = {}
NEXT_ID = 2


def create_user(name: str, email: str, password: str, role: Role) -> User:
    """Cria somente papéis públicos e rejeita e-mail duplicado."""
    global NEXT_ID
    if any(u.email == email.lower() for u in USERS.values()):
        raise ValueError("E-mail já cadastrado")
    user = User(NEXT_ID, name, email.lower(), role, hash_password(password))
    USERS[NEXT_ID] = user
    NEXT_ID += 1
    return user


def authenticate(email: str, password: str) -> str | None:
    """Emite token opaco somente após verificação da senha."""
    user = next((u for u in USERS.values() if u.email == email.lower()), None)
    if user and user.active and verify_password(password, user.password_hash):
        token = secrets.token_urlsafe(32)
        TOKENS[token] = user.id
        return token
    return None


def find_by_token(token: str) -> User | None:
    user_id = TOKENS.get(token)
    return USERS.get(user_id) if user_id else None


def revoke(token: str) -> None:
    TOKENS.pop(token, None)
