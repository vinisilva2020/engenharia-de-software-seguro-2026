"""Cliente interno para comunicação com o serviço de pagamentos.

O timeout e o circuit breaker serão adicionados pela Pessoa 4. Neste commit,
este módulo apenas define o contrato de comunicação e a idempotência.
"""

from dataclasses import dataclass

import httpx
from fastapi import HTTPException
from app.services.circuit_breaker import circuit_breaker, CircuitOpenError


@dataclass(frozen=True)
class PaymentClient:
    base_url: str = "http://127.0.0.1:8001"

    def create_payment(self, order_id: int, amount: float) -> dict:
        """Solicita pagamento usando uma chave estável por pedido."""
        payload = {"order_id": order_id, "amount": amount, "currency": "BRL"}
        headers = {"Idempotency-Key": f"order-{order_id}"}
        try:
            circuit_breaker.before_call()
            with httpx.Client(base_url=self.base_url, timeout=3) as client: response = client.post("/api/v1/payments", json=payload, headers=headers)
            response.raise_for_status()
        except CircuitOpenError as exc: raise HTTPException(503, "Circuito aberto: pagamento bloqueado") from exc
        except httpx.HTTPError as exc:
            circuit_breaker.failure(); raise HTTPException(503, "Serviço de pagamento indisponível") from exc
        circuit_breaker.success()
        return response.json()

    def get_payment(self, payment_id: str) -> dict:
        """Consulta o status de uma transação existente."""
        with httpx.Client(base_url=self.base_url) as client:
            response = client.get(f"/api/v1/payments/{payment_id}")
        response.raise_for_status()
        return response.json()

