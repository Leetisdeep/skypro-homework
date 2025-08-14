import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def category() -> "Category":
    # Сбросим счетчики перед каждым тестом
    Category.total_categories = 0
    Category.total_unique_products = 0
    product1 = Product("Samsung Galaxy S23 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return Category("Смартфоны", "Смартфоны", [product1, product2])


def test_init(category: Category) -> None:
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны"
    assert len(category.products) == 2
    assert Category.total_categories == 1
    assert Category.total_unique_products == 2


def test_products_property(category: Category) -> None:
    products_str = category.products
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in products_str
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in products_str


def test_add_product(category: Category) -> None:
    initial_count = Category.total_unique_products
    new_product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category.add_product(new_product)
    assert Category.total_unique_products == initial_count + 1
    assert len(category.products) == 3


def test_category_str(category: Category) -> None:
    assert str(category) == "Смартфоны, количество продуктов: 13 шт."


def test_add_duplicate_product(category: Category) -> None:
    initial_count = Category.total_unique_products
    duplicate_product = Product("Samsung Galaxy S23 Ultra",
                              "256GB, Серый цвет, 200MP камера",
                              180000.0, 3)
    category.add_product(duplicate_product)
    # Количество уникальных продуктов не должно измениться
    assert Category.total_unique_products == initial_count
    # Но общее количество товаров в категории увеличится
    assert str(category) == "Смартфоны, количество продуктов: 16 шт."


def test_average_price(category: Category) -> None:
    assert category.average_price() == (180000.0 + 210000.0) / 2


def test_average_price_empty_category() -> None:
    empty_category = Category("Пустая", "Пустая категория", [])
    assert empty_category.average_price() == 0


def test_add_invalid_product(category: Category) -> None:
    with pytest.raises(TypeError):
        category.add_product("Not a product")
