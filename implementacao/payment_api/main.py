"""API independente para simulação de pagamentos.

Este serviço não recebe senha nem dados completos de cartão. Ele trabalha
somente com o identificador do pedido, valor calculado pelo backend e uma
chave de idempotência.
"""

from dataclasses import dataclass, asdict
from datetime import UTC, datetime
from enum import StrEnum
from secrets import token_urlsafe

from fastapi import FastAPI, Header, HTTPException, status
from pydantic import BaseModel, Field


class PaymentStatus(StrEnum):
    PENDING = "pending"
    APPROVED = "approved"
    DECLINED = "declined"


@dataclass
class Payment:
    id: str
    order_id: int
    amount: float
    currency: str
    status: PaymentStatus
    created_at: str


class PaymentRequest(BaseModel):
    """Dados mínimos para criar uma transação."""

    order_id: int = Field(gt=0)
    amount: float = Field(gt=0, le=100_000)
    currency: str = Field(default="BRL", pattern=r"^[A-Z]{3}$")


class PaymentResponse(BaseModel):
    id: str
    order_id: int
    amount: float
    currency: str
    status: PaymentStatus
    created_at: str


app = FastAPI(title="Delivery Seguro — Payment API", version="1.0.0")
PAYMENTS: dict[str, Payment] = {}
IDEMPOTENCY_INDEX: dict[str, str] = {}


def response(payment: Payment) -> PaymentResponse:
    """Converte o modelo interno em uma resposta pública controlada."""
    return PaymentResponse(**asdict(payment))


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok", "service": "payment-api"}


@app.post(
    "/api/v1/payments",
    response_model=PaymentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["payments"],
)
def create_payment(
    data: PaymentRequest,
    idempotency_key: str | None = Header(default=None, alias="Idempotency-Key"),
) -> PaymentResponse:
    """Cria uma cobrança sem duplicá-la quando a requisição é repetida.

    A mesma chave retorna a mesma transação. Isso protege contra novas
    cobranças quando o cliente repete uma requisição após timeout ou retry.
    """
    if not idempotency_key or not idempotency_key.strip():
        raise HTTPException(400, "O cabeçalho Idempotency-Key é obrigatório")
    if len(idempotency_key) > 128:
        raise HTTPException(400, "Idempotency-Key excede o tamanho permitido")

    existing_id = IDEMPOTENCY_INDEX.get(idempotency_key)
    if existing_id is not None:
        return response(PAYMENTS[existing_id])

    payment = Payment(
        id=f"pay_{token_urlsafe(12)}",
        order_id=data.order_id,
        amount=round(data.amount, 2),
        currency=data.currency,
        status=PaymentStatus.APPROVED,
        created_at=datetime.now(UTC).isoformat(),
    )
    PAYMENTS[payment.id] = payment
    IDEMPOTENCY_INDEX[idempotency_key] = payment.id
    return response(payment)


@app.get("/api/v1/payments/{payment_id}", response_model=PaymentResponse, tags=["payments"])
def get_payment(payment_id: str) -> PaymentResponse:
    """Consulta uma transação sem expor credenciais ou dados financeiros sensíveis."""
    payment = PAYMENTS.get(payment_id)
    if payment is None:
        raise HTTPException(404, "Pagamento não encontrado")
    return response(payment)

