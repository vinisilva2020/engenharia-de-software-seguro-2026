from decimal import Decimal
from fastapi import HTTPException
from app.services.catalog import MENU_ITEMS, find_establishment
from app.services.payment_client import PaymentClient

ORDERS, NEXT_ID = {}, 1

def create_order(user_id, establishment_id, items):
    global NEXT_ID
    if not items: raise HTTPException(400, "Carrinho vazio")
    establishment = find_establishment(establishment_id)
    if not establishment: raise HTTPException(404, "Estabelecimento não encontrado")
    catalog = {x.id: x for x in MENU_ITEMS}; normalized=[]; total=Decimal("0")
    for item in items:
        product, quantity = catalog.get(item.get("product_id")), item.get("quantity")
        if not product or product.establishment_id != establishment_id: raise HTTPException(400, "Produto inválido para este estabelecimento")
        if isinstance(quantity, bool) or not isinstance(quantity, int) or not 1 <= quantity <= 20: raise HTTPException(400, "Quantidade inválida")
        subtotal = Decimal(str(product.price)) * quantity; total += subtotal
        normalized.append({"product_id": product.id, "name": product.name, "unit_price": product.price, "quantity": quantity, "subtotal": float(subtotal.quantize(Decimal('.01')))})
    order={"id":NEXT_ID,"user_id":user_id,"establishment_id":establishment_id,"establishment_name":establishment.name,"items":normalized,"total":float(total.quantize(Decimal('.01'))),"status":"pending_payment"}
    payment = PaymentClient().create_payment(order["id"], order["total"])
    order.update({"status": "paid", "payment_id": payment["id"]})
    ORDERS[NEXT_ID]=order; NEXT_ID+=1; return order

def user_orders(user_id): return [x for x in ORDERS.values() if x["user_id"] == user_id]
