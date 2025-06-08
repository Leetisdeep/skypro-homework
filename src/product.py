class Product:
    def __init__(self, name: str, description: str,
                 price: float, quantity: int):
        if quantity <= 0:
            raise ValueError(
                "Товар с нулевым количеством не может быть добавлен"
            )

        self.name = name
        self.description = description
        self._price = price  # Using protected attribute for price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        """Создает новый продукт из словаря"""
        return cls(
            name=product_data['name'],
            description=product_data['description'],
            price=product_data['price'],
            quantity=product_data['quantity']
        )

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        self._price = new_price

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только продукты класса Product")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
