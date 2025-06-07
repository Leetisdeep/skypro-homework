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
    """
    Класс, представляющий категорию товаров.
    """

    # Атрибуты класса для подсчета количества категорий и уникальных продуктов
    category_count = 0
    product_count = 0
    _unique_products = set()

    def __init__(self, name, description, products):
        """
        Инициализация категории.
        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов в категории
        """
        self.name = name
        self.description = description
        self.__products: List[Product] = list(products) if products else []
        self.products = products

        # обновляем счётчики
        # Увеличиваем счетчик категорий
        Category.category_count += 1
        Category._unique_products.update(p.name for p in self.__products)
        Category.product_count = len(Category._unique_products)

    # read-only доступ к товарам
    @property
    def products(self) -> tuple[Product, ...]:
        return tuple(self.__products)
        # Добавляем продукты в множество уникальных продуктов
        for product in products:
            Category._unique_products.add(product)

        # Обновляем счетчик уникальных продуктов
        Category.product_count = len(Category._unique_products)

    # ───── строковое представление (из условия ДЗ) ───────────────────────────
    def str(self) -> str:
        total_qty = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_qty} шт."
    def __repr__(self):
        return f"Category(name={self.name}, products={self.products})"
