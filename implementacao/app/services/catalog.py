"""Catálogo fixo usado pela primeira etapa da implementação.

Os dados são estáticos para a demonstração. A camada expõe somente informações
de catálogo; regras de criação e alteração de pedidos serão implementadas em
uma etapa posterior.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Establishment:
    id: int
    name: str
    description: str


@dataclass(frozen=True)
class MenuItem:
    id: int
    establishment_id: int
    name: str
    description: str
    price: float
    available: bool = True


ESTABLISHMENTS: tuple[Establishment, ...] = (
    Establishment(1, "Pampa Burger", "Hambúrgueres artesanais"),
    Establishment(2, "Alegrete Massas", "Massas e pratos caseiros"),
)

MENU_ITEMS: tuple[MenuItem, ...] = (
    MenuItem(1, 1, "Hambúrguer artesanal", "Pão, carne, queijo e molho da casa", 32.90),
    MenuItem(2, 1, "Batata frita", "Porção individual crocante", 14.90),
    MenuItem(3, 1, "Refrigerante", "Lata 350 ml", 7.00),
    MenuItem(4, 2, "Lasanha à bolonhesa", "Lasanha caseira com molho de tomate", 34.90),
    MenuItem(5, 2, "Espaguete caseiro", "Massa artesanal ao molho da casa", 29.90),
    MenuItem(6, 2, "Suco natural", "Suco natural do dia", 9.00),
)


def list_establishments() -> tuple[Establishment, ...]:
    """Retorna os estabelecimentos disponíveis para seleção."""
    return ESTABLISHMENTS


def find_establishment(establishment_id: int) -> Establishment | None:
    """Busca um estabelecimento pelo identificador informado na URL."""
    return next((item for item in ESTABLISHMENTS if item.id == establishment_id), None)


def list_menu(establishment_id: int | None = None) -> tuple[MenuItem, ...]:
    """Retorna o cardápio completo ou apenas o cardápio de um estabelecimento."""
    if establishment_id is None:
        return MENU_ITEMS
    return tuple(
        item for item in MENU_ITEMS if item.establishment_id == establishment_id
    )
