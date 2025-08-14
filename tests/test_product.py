import pytest
from src.product import Product
from src.category import Smartphone, LawnGrass


@pytest.fixture
def product() -> "Product":
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )


def test_init(product: Product) -> None:
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product() -> None:
    product_dict = {
        "name": "Xiaomi Redmi Note 12",
        "description": "128GB, Blue",
        "price": 25000.0,
        "quantity": 10
    }
    product = Product.new_product(product_dict)
    assert product.name == "Xiaomi Redmi Note 12"
    assert product.price == 25000.0
    assert product.quantity == 10


def test_price_setter(product: Product) -> None:
    product.price = 200000.0
    assert product.price == 200000.0
    
    # Проверка на отрицательную цену
    with pytest.raises(ValueError):
        product.price = -1000.0
    assert product.price == 200000.0  # Цена не изменилась


def test_product_str(product: Product) -> None:
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add() -> None:
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    assert product1 + product2 == 50000.0 * 10 + 100000.0 * 5


def test_product_add_type_error(product: Product) -> None:
    with pytest.raises(TypeError):
        product + "Не продукт"


def test_product_zero_quantity() -> None:
    with pytest.raises(ValueError):
        Product("Тест", "Тест", 100, 0)


@pytest.fixture
def smartphone() -> "Smartphone":
    return Smartphone(
        "iPhone 15 Pro",
        "512GB, Titanium",
        200000.0,
        3,
        1.5,
        "15 Pro",
        512,
        "Titanium"
    )


@pytest.fixture
def lawn_grass() -> "LawnGrass":
    return LawnGrass(
        "Premium Grass",
        "Soft and durable lawn grass",
        500.0,
        100,
        "USA",
        "2 weeks",
        "Dark green"
    )


def test_smartphone_add(smartphone: Smartphone) -> None:
    smartphone2 = Smartphone(
        "iPhone 15",
        "256GB, Titanium",
        150000.0,
        5,
        1.2,
        "15",
        256,
        "Titanium"
    )
    assert smartphone + smartphone2 == 200000.0 * 3 + 150000.0 * 5


def test_lawn_grass_add(lawn_grass: LawnGrass) -> None:
    lawn_grass2 = LawnGrass(
        "Standard Grass",
        "Basic lawn grass",
        300.0,
        50,
        "Canada",
        "3 weeks",
        "Light green"
    )
    assert lawn_grass + lawn_grass2 == 500.0 * 100 + 300.0 * 50


def test_smartphone_new_product() -> None:
    product_dict = {
        "name": "Xiaomi Redmi Note 12",
        "description": "128GB, Blue",
        "price": 25000.0,
        "quantity": 10,
        "efficiency": 1.0,
        "model": "Note 12",
        "memory": 128,
        "color": "Blue"
    }
    product = Smartphone.new_product(product_dict)
    assert isinstance(product, Smartphone)
    assert product.model == "Note 12"


def test_lawn_grass_new_product() -> None:
    product_dict = {
        "name": "Eco Grass",
        "description": "Environment friendly",
        "price": 400.0,
        "quantity": 200,
        "country": "Germany",
        "germination_period": "10 days",
        "color": "Bright green"
    }
    product = LawnGrass.new_product(product_dict)
    assert isinstance(product, LawnGrass)
    assert product.country == "Germany"
