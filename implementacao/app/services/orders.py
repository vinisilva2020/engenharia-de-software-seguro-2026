"""Regras de criação de pedidos e proteção contra tampering.

Esta etapa ainda não processa pagamentos. O pedido é criado com status
``pending_payment`` para que a integração com o serviço de pagamentos seja
adicionada posteriormente.
"""

from decimal import Decimal, ROUND_HALF_UP

from fastapi import HTTPException

from app.services.catalog import ESTABLISHMENTS, MENU_ITEMS, find_establishment

ORDERS: dict[int, dict] = {}
_next_order_id = 1


def _money(value: float | int | Decimal) -> Decimal:
    """Normaliza valores monetários com duas casas decimais."""
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def create_order(user_id: int, establishment_id: int, items: list[dict]) -> dict:
    """Cria pedido usando exclusivamente os preços oficiais do catálogo.

    O método ignora qualquer ``price`` ou ``subtotal`` enviado pelo cliente,
    valida o estabelecimento de cada produto e calcula todos os totais no
    servidor. Essa é a proteção principal contra R05 — Tampering de Pedidos.
    """
    global _next_order_id

    if not items:
        raise HTTPException(status_code=400, detail="O carrinho não pode estar vazio")

    establishment = find_establishment(establishment_id)
    if establishment is None:
        raise HTTPException(status_code=404, detail="Estabelecimento não encontrado")

    normalized_items = []
    total = Decimal("0.00")
    catalog_by_id = {item.id: item for item in MENU_ITEMS}

    for received_item in items:
        product_id = received_item.get("product_id")
        quantity = received_item.get("quantity")
        product = catalog_by_id.get(product_id)

        if product is None or product.establishment_id != establishment_id:
            raise HTTPException(
                status_code=400,
                detail="Produto inválido para o estabelecimento selecionado",
            )
        if (
            not isinstance(quantity, int)
            or isinstance(quantity, bool)
            or not 1 <= quantity <= 20
        ):
            raise HTTPException(
                status_code=400, detail="Quantidade deve estar entre 1 e 20"
            )
        if not product.available:
            raise HTTPException(status_code=400, detail="Produto indisponível")

        unit_price = _money(product.price)
        subtotal = _money(unit_price * quantity)
        total += subtotal
        normalized_items.append(
            {
                "product_id": product.id,
                "name": product.name,
                "unit_price": float(unit_price),
                "quantity": quantity,
                "subtotal": float(subtotal),
            }
        )

    order = {
        "id": _next_order_id,
        "user_id": user_id,
        "establishment_id": establishment.id,
        "establishment_name": establishment.name,
        "items": normalized_items,
        "total": float(_money(total)),
        "status": "pending_payment",
    }
    ORDERS[_next_order_id] = order
    _next_order_id += 1
    return order


def list_user_orders(user_id: int) -> list[dict]:
    """Retorna somente pedidos pertencentes ao usuário autenticado."""
    return [order for order in ORDERS.values() if order["user_id"] == user_id]
