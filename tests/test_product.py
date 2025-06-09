import pytest
from src.product import Product
from src.category import Category, Smartphone, LawnGrass

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


def test_new_product(product: Product) -> None:
    new_dict = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    ret = product.new_product(new_dict)
    assert ret.name == "Samsung Galaxy S23 Ultra"


def test_price(product: Product) -> None:
    assert product.price == 180000.0
    product.price = 50
    assert product.price == 50
    with pytest.raises(ValueError):  # Теперь ожидаем ошибку
        product.price = -50
    assert product.price == 50  # Цена не изменилась


def test_product_str():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    assert str(product) == "Телефон, 50000.0 руб. Остаток: 10 шт."


def test_product_add():
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    assert product1 + product2 == 50000.0 * 10 + 100000.0 * 5


def test_product_add_type_error():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    with pytest.raises(TypeError):
        product + "Не продукт"


def test_product_price_setter_positive():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    product.price = 60000.0
    assert product.price == 60000.0


def test_product_price_setter_negative_or_zero():
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    with pytest.raises(
            ValueError,
            match="Цена не должна быть нулевая или отрицательная"
    ):
        product.price = -1000.0
    assert product.price == 50000.0  # Цена не изменилась


def test_product_zero_quantity():
    """Тест создания продукта с нулевым количеством"""
    with pytest.raises(
            ValueError,
            match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Тест", "Тест", 100, 0)


def test_category_average_price():
    """Тест расчета средней цены категории"""
    # Случай с товарами
    p1 = Product("Товар 1", "Описание", 100, 10)
    p2 = Product("Товар 2", "Описание", 200, 5)
    cat = Category("Категория", "Описание", [p1, p2])
    assert cat.average_price() == 150.0

    # Случай без товаров
    empty_cat = Category("Пустая", "Описание", [])
    assert empty_cat.average_price() == 0

    # Случай с нулевой ценой
    p3 = Product("Товар 3", "Описание", 0, 1)
    cat_with_zero = Category("С нулем", "Описание", [p3])
    assert cat_with_zero.average_price() == 0


def test_add_product_with_zero_quantity():
    """Тест добавления продукта с нулевым количеством через new_product"""
    with pytest.raises(ValueError):
        Product.new_product({
            "name": "Тест",
            "description": "Тест",
            "price": 100,
            "quantity": 0
        })

import pytest
from src.product import Smartphone, LawnGrass


@pytest.fixture
def smartphone() -> "Smartphone":
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        1.2,
        "S23 Ultra",
        256,
        "Gray"
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


def test_smartphone_init(smartphone: Smartphone) -> None:
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 1.2
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Gray"


def test_lawn_grass_init(lawn_grass: LawnGrass) -> None:
    assert lawn_grass.name == "Premium Grass"
    assert lawn_grass.description == "Soft and durable lawn grass"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 100
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "2 weeks"
    assert lawn_grass.color == "Dark green"


def test_smartphone_str(smartphone: Smartphone) -> None:
    assert str(smartphone) == ("Samsung Galaxy S23 Ultra, 180000.0 руб. "
                              "Остаток: 5 шт.")


def test_lawn_grass_str(lawn_grass: LawnGrass) -> None:
    assert str(lawn_grass) == ("Premium Grass, 500.0 руб. Остаток: 100 шт.")


def test_smartphone_price(smartphone: Smartphone) -> None:
    assert smartphone.price == 180000.0
    smartphone.price = 50
    assert smartphone.price == 50
    with pytest.raises(ValueError):
        smartphone.price = -50
    assert smartphone.price == 50  # Цена не изменилась


def test_lawn_grass_price(lawn_grass: LawnGrass) -> None:
    assert lawn_grass.price == 500.0
    lawn_grass.price = 400
    assert lawn_grass.price == 400
    with pytest.raises(ValueError):
        lawn_grass.price = 0
    assert lawn_grass.price == 400  # Цена не изменилась


def test_smartphone_add(smartphone: Smartphone) -> None:
    smartphone2 = Smartphone(
        "iPhone 15 Pro",
        "512GB, Titanium",
        200000.0,
        3,
        1.5,
        "15 Pro",
        512,
        "Titanium"
    )
    assert smartphone + smartphone2 == 180000.0 * 5 + 200000.0 * 3


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


def test_smartphone_add_type_error(smartphone: Smartphone) -> None:
    with pytest.raises(TypeError):
        smartphone + "Не продукт"


def test_lawn_grass_add_type_error(lawn_grass: LawnGrass) -> None:
    with pytest.raises(TypeError):
        lawn_grass + 100


def test_smartphone_new_product() -> None:
    new_dict = {
        "name": "Xiaomi Redmi Note 12",
        "description": "128GB, Blue",
        "price": 25000.0,
        "quantity": 10,
        "efficiency": 1.0,
        "model": "Note 12",
        "memory": 128,
        "color": "Blue"
    }
    product = Smartphone.new_product(new_dict)
    assert product.name == "Xiaomi Redmi Note 12"
    assert product.price == 25000.0
    assert product.model == "Note 12"


def test_lawn_grass_new_product() -> None:
    new_dict = {
        "name": "Eco Grass",
        "description": "Environment friendly",
        "price": 400.0,
        "quantity": 200,
        "country": "Germany",
        "germination_period": "10 days",
        "color": "Bright green"
    }
    product = LawnGrass.new_product(new_dict)
    assert product.name == "Eco Grass"
    assert product.price == 400.0
    assert product.country == "Germany"


def test_smartphone_zero_quantity() -> None:
    with pytest.raises(
            ValueError,
            match="Товар с нулевым количеством не может быть добавлен"
    ):
        Smartphone(
            "Test Phone",
            "Test",
            10000.0,
            0,
            1.0,
            "Test",
            64,
            "Black"
        )


def test_lawn_grass_zero_quantity() -> None:
    with pytest.raises(
            ValueError,
            match="Товар с нулевым количеством не может быть добавлен"
    ):
        LawnGrass(
            "Test Grass",
            "Test",
            100.0,
            0,
            "Test",
            "Test",
            "Test"
        )


def test_smartphone_repr(smartphone: Smartphone) -> None:
    assert repr(smartphone).startswith("<Smartphone(")
    assert "name='Samsung Galaxy S23 Ultra'" in repr(smartphone)
    assert "price=180000.0" in repr(smartphone)
    assert "memory=256" in repr(smartphone)


def test_lawn_grass_repr(lawn_grass: LawnGrass) -> None:
    assert repr(lawn_grass).startswith("<LawnGrass(")
    assert "name='Premium Grass'" in repr(lawn_grass)
    assert "price=500.0" in repr(lawn_grass)
    assert "country='USA'" in repr(lawn_grass)
