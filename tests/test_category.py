import pytest
from src.category import Category
from src.product import Product

@pytest.fixture()
def category() -> "Category":
    # Сбросим счетчики перед каждым тестом
    Category.all_category = 0
    Category.all_products = 0  # Исправлено имя
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return Category("Смартфоны", "Смартфоны", [product1, product2])

def test_init(category: Category) -> None:
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны"
    assert len(category.products.split("\n")) == 2  # Исправлено: работаем со строкой
    assert Category.all_category == 1
    assert Category.all_products == 2  # Исправлено имя

def test_products_property(category: Category) -> None:
    products_str = category.products
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in products_str
    assert "Iphone 15, 210000.0 руб. Остаток: 8 шт." in products_str

def test_add_product(category: Category) -> None:
    initial_count = Category.all_products  # Исправлено имя
    new_product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category.add_product(new_product)
    assert Category.all_products == initial_count + 1  # Исправлено имя
    assert len(category.products.split("\n")) == 3  # Исправлено: работаем со строкой

def test_category_str(category: Category) -> None:
    assert str(category) == "Смартфоны, количество продуктов: 13 шт."

def test_average_price(category: Category) -> None:
    assert category.average_price() == (180000.0 + 210000.0) / 2

def test_average_price_empty_category() -> None:
    empty_category = Category("Пустая", "Пустая категория", [])
    assert empty_category.average_price() == 0

def test_add_invalid_product(category: Category) -> None:
    with pytest.raises(TypeError):
        category.add_product("Not a product")
