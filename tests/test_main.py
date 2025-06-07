from main import Product, Category


def test_category_counts():
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
    # Создаем категории
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
    # Проверяем счетчики
    assert Category.category_count == 2  # Две категории созданы
    assert Category.product_count == 2  # Два уникальных продукта
