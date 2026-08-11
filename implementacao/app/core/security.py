"""Ponto reservado para autenticação, autorização e políticas de segurança."""

"""Controles de segurança: hash de senhas, tokens e autorização RBAC."""

import hashlib
import hmac
import secrets
from dataclasses import dataclass
from enum import StrEnum
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


class Role(StrEnum):
    """Papéis válidos; o cliente nunca escolhe administrador."""

    CLIENTE = "cliente"
    ENTREGADOR = "entregador"
    ESTABELECIMENTO = "estabelecimento"
    ADMINISTRADOR = "administrador"


@dataclass
class User:
    """Entidade interna; password_hash jamais deve ser serializado na API."""

    id: int
    name: str
    email: str
    role: Role
    password_hash: str
    active: bool = True


def hash_password(password: str) -> str:
    """Armazena apenas derivação lenta com salt único, nunca a senha original."""
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 210_000)
    return f"pbkdf2_sha256$210000${salt.hex()}${digest.hex()}"


def verify_password(password: str, encoded: str) -> bool:
    """Compara hashes em tempo constante e falha fechado para formato inválido."""
    try:
        algorithm, rounds, salt, expected = encoded.split("$")
        candidate = hashlib.pbkdf2_hmac(
            algorithm.removeprefix("pbkdf2_"),
            password.encode(),
            bytes.fromhex(salt),
            int(rounds),
        )
        return hmac.compare_digest(candidate.hex(), expected)
    except (ValueError, TypeError):
        return False


bearer = HTTPBearer(auto_error=False)


def current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer),
) -> User:
    """Autentica toda requisição protegida antes de qualquer regra de negócio."""
    from app.repositories.users import find_by_token

    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(401, "Autenticação necessária")
    user = find_by_token(credentials.credentials)
    if user is None or not user.active:
        raise HTTPException(401, "Token inválido ou revogado")
    return user


def require_roles(*roles: Role):
    """Dependency de negação por padrão: somente papéis explicitamente listados passam."""

    def check(user: User = Depends(current_user)) -> User:
        if user.role not in roles:
            raise HTTPException(403, "Permissão insuficiente")
        return user

    return check
