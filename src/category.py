from src.product import Product


class Category:
    """Класс категории товаров"""

    all_category = 0
    all_product = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self._products = []

        for product in products:
            self.add_product(product)

        Category.all_category += 1

    @property
    def products(self) -> str:
        """Форматирует информацию о продуктах для вывода"""
        product_strings = []
        for product in self._products:
            product_str = (f"{product.name}, {product.price} руб. "
                          f"Остаток: {product.quantity} шт. ")
            product_strings.append(product_str)
        return "".join(product_strings)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию"""
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )
        self._products.append(product)
        Category.all_product += 1

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def average_price(self) -> float:
        """Метод расчета средней цены товаров в категории"""
        if not self._products:
            return 0

        try:
            total = sum(product.price for product in self._products)
            return total / len(self._products)
        except ZeroDivisionError:
            return 0
