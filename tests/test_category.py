from src.product import Product
from src.category import Category


def test_category_counters():
    """
    Тест подсчета количества категорий и уникальных продуктов.
    """
    product1 = Product(
        name="Laptop",
        description="A powerful laptop",
        price=1000,
        quantity=5
    )
    product2 = Product(
        name="Smartphone",
        description="A modern smartphone",
        price=500,
        quantity=10
    )

    Category(
        name="Electronics",
        description="All electronic devices",
        products=[product1, product2]
    )
    Category(
        name="Books",
        description="All books",
        products=[product1]
    )

    assert Category.category_count == 2  # Две категории созданы
    assert Category.product_count == 2   # Два уникальных продукта
