from src.product import Product


def test_product_creation():
    """
    Тест создания объекта Product.
    """
    product = Product(
        name="Laptop",
        description="A powerful laptop",
        price=1000,
        quantity=5
    )

    assert product.name == "Laptop"
    assert product.description == "A powerful laptop"
    assert product.price == 1000
    assert product.quantity == 5


def test_product_repr():
    """
    Тест метода __repr__ для Product.
    """
    product = Product(
        name="Smartphone",
        description="A modern smartphone",
        price=500,
        quantity=10
    )

    expected_repr = "Product(name=Smartphone, price=500, quantity=10)"
    assert repr(product) == expected_repr
