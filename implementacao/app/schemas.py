from pydantic import BaseModel, EmailStr, Field


class Credentials(BaseModel):
    email: EmailStr
    password: str


class Registration(Credentials):
    name: str = Field(min_length=2, max_length=100)
    password: str = Field(min_length=12, max_length=128)


class PublicUser(BaseModel):
    """Allowlist de resposta: nunca inclui hash, token, senha ou dados internos."""

    id: int
    name: str
    email: EmailStr
    role: str
