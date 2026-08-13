"""Cliente interno para comunicação com o serviço de pagamentos.

O timeout e o circuit breaker serão adicionados pela Pessoa 4. Neste commit,
este módulo apenas define o contrato de comunicação e a idempotência.
"""

from dataclasses import dataclass

import httpx


@dataclass(frozen=True)
class PaymentClient:
    base_url: str = "http://127.0.0.1:8001"

    def create_payment(self, order_id: int, amount: float) -> dict:
        """Solicita pagamento usando uma chave estável por pedido."""
        payload = {"order_id": order_id, "amount": amount, "currency": "BRL"}
        headers = {"Idempotency-Key": f"order-{order_id}"}
        with httpx.Client(base_url=self.base_url) as client:
            response = client.post("/api/v1/payments", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_payment(self, payment_id: str) -> dict:
        """Consulta o status de uma transação existente."""
        with httpx.Client(base_url=self.base_url) as client:
            response = client.get(f"/api/v1/payments/{payment_id}")
        response.raise_for_status()
        return response.json()

