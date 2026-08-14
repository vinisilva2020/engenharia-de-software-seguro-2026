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


class OrderItemRequest(BaseModel):
    """Item recebido do cliente; o preço nunca é aceito da requisição."""

    product_id: int
    quantity: int = Field(ge=1, le=20)


class OrderRequest(BaseModel):
    """Pedido mínimo para criação do carrinho no servidor."""

    establishment_id: int
    items: list[OrderItemRequest] = Field(min_length=1)
