# src/category.py
from typing import Iterable, List

from .product import Product


class Category:
    """Категория товаров."""

    # ───── глобальные счётчики ────────────────────────────────────────────────
    category_count: int = 0          # сколько категорий создано
    _unique_products: set[str] = set()
    product_count: int = 0           # количество уникальных товаров

    # ──────────────────────────────────────────────────────────────────────────
    def init(
        self,
        name: str,
        description: str = "",
        products: Iterable[Product] | None = None,
    ) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = list(products) if products else []

        # обновляем счётчики
        Category.category_count += 1
        Category._unique_products.update(p.name for p in self.__products)
        Category.product_count = len(Category._unique_products)

    # read-only доступ к товарам
    @property
    def products(self) -> tuple[Product, ...]:
        return tuple(self.__products)

    # ───── строковое представление (из условия ДЗ) ───────────────────────────
    def str(self) -> str:
        total_qty = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_qty} шт."
