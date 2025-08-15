import pytest
from main import Category, Product


@pytest.fixture(autouse=True)
def reset_total_products():
    """Сбрасывает значение total_products перед каждым тестом."""
    Category.total_products = 0


# Тесты для класса Category
def test_add_product():
    """Тест добавления продукта в категорию."""
    category = Category()
    product_data = {"name": "Телефон", "price": 10000, "quantity": 5}
    product = Product.new_product(product_data)
    category.add_product(product)
    expected = "Телефон, 10000 руб. Остаток: 5 шт.\n"
    assert category.products == expected


def test_add_duplicate_product():
    """Тест добавления дубликата продукта."""
    category = Category()
    product1 = Product.new_product(
        {"name": "Телефон", "price": 10000, "quantity": 5}
    )
    product2 = Product.new_product(
        {"name": "Телефон", "price": 12000, "quantity": 3}
    )
    category.add_product(product1)
    category.add_product(product2)
    expected = "Телефон, 12000 руб. Остаток: 8 шт.\n"
    assert category.products == expected


def test_total_products_counter(reset_total_products):
    """Тест счетчика продуктов."""
    category = Category()
    product1 = Product.new_product(
        {"name": "Телефон", "price": 10000, "quantity": 5}
    )
    product2 = Product.new_product(
        {"name": "Ноутбук", "price": 50000, "quantity": 2}
    )
    category.add_product(product1)
    category.add_product(product2)
    assert Category.total_products == 2


# Тесты для класса Product
def test_new_product_creation():
    """Тест создания нового продукта через класс-метод."""
    data = {"name": "Книга", "price": 500, "quantity": 20}
    product = Product.new_product(data)
    assert product.name == "Книга"
    assert product.price == 500
    assert product.quantity == 20


def test_price_validation():
    """Тест проверки цены (недопустимые значения)."""
    product = Product("Ноутбук", 50000, 10)
    product.price = -1000  # Попытка установить недопустимую цену
    assert product.price == 50000  # Цена не должна измениться


def test_price_reduction_confirmation(monkeypatch):
    """Тест понижения цены с подтверждением."""
    product = Product("Ноутбук", 50000, 10)
    # Моделируем ввод пользователя ("n" для отмены)
    monkeypatch.setattr('builtins.input', lambda _: "n")
    product.price = 45000
    assert product.price == 50000  # Цена не должна измениться

    # Моделируем ввод пользователя ("y" для подтверждения)
    monkeypatch.setattr('builtins.input', lambda _: "y")
    product.price = 45000
    assert product.price == 45000  # Цена должна измениться


def test_category_products_property():
    """Тест свойства products в классе Category."""
    category = Category()
    product1 = Product.new_product(
        {"name": "Телефон", "price": 10000, "quantity": 5}
    )
    product2 = Product.new_product(
        {"name": "Ноутбук", "price": 50000, "quantity": 2}
    )
    category.add_product(product1)
    category.add_product(product2)
    expected = (
        "Телефон, 10000 руб. Остаток: 5 шт.\n"
        "Ноутбук, 50000 руб. Остаток: 2 шт.\n"
    )
    assert category.products == expected
