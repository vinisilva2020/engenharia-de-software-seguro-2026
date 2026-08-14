"""Criação de pedidos com validação no servidor e pagamento protegido."""

from decimal import Decimal, ROUND_HALF_UP

from fastapi import HTTPException

from app.services.catalog import MENU_ITEMS, find_establishment
from app.services.payment_client import PaymentClient

ORDERS: dict[int, dict] = {}
_next_order_id = 1


def _money(value: float | int | Decimal) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def create_order(user_id: int, establishment_id: int, items: list[dict]) -> dict:
    """Calcula o pedido com preços oficiais e solicita seu pagamento."""
    global _next_order_id
    if not items:
        raise HTTPException(400, "O carrinho não pode estar vazio")
    establishment = find_establishment(establishment_id)
    if establishment is None:
        raise HTTPException(404, "Estabelecimento não encontrado")

    normalized_items = []
    total = Decimal("0.00")
    catalog = {item.id: item for item in MENU_ITEMS}
    for received in items:
        product = catalog.get(received.get("product_id"))
        quantity = received.get("quantity")
        if product is None or product.establishment_id != establishment_id:
            raise HTTPException(400, "Produto inválido para o estabelecimento selecionado")
        if (not isinstance(quantity, int) or isinstance(quantity, bool)
                or not 1 <= quantity <= 20):
            raise HTTPException(400, "Quantidade deve estar entre 1 e 20")
        if not product.available:
            raise HTTPException(400, "Produto indisponível")
        unit_price = _money(product.price)
        subtotal = _money(unit_price * quantity)
        total += subtotal
        normalized_items.append({
            "product_id": product.id, "name": product.name,
            "unit_price": float(unit_price), "quantity": quantity,
            "subtotal": float(subtotal),
        })

    order = {
        "id": _next_order_id, "user_id": user_id,
        "establishment_id": establishment.id,
        "establishment_name": establishment.name,
        "items": normalized_items, "total": float(_money(total)),
        "status": "pending_payment",
    }
    payment = PaymentClient().create_payment(order["id"], order["total"])
    order.update({"status": "paid", "payment_id": payment["id"]})
    ORDERS[_next_order_id] = order
    _next_order_id += 1
    return order


def user_orders(user_id: int) -> list[dict]:
    return [order for order in ORDERS.values() if order["user_id"] == user_id]


def list_user_orders(user_id: int) -> list[dict]:
    """Alias compatível com a versão recebida do repositório remoto."""
    return user_orders(user_id)
