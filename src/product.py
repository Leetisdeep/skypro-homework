class Product:
    """
    Класс, представляющий продукт.
    """
    def __init__(self, name, description, price, quantity):
        """
        Инициализация продукта.
        """
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для цены с проверками."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if value < self.__price:
            confirmation = input("Вы уверены, что хотите понизить цену? (y/n): ")
            if confirmation.lower() != "y":
                print("Изменение цены отменено")
                return
        self.__price = value

    @classmethod
    def new_product(cls, data):
        """Создание нового продукта из словаря."""
        if not isinstance(data, dict):
            raise ValueError("Данные должны быть переданы в виде словаря")
        required_keys = {"name", "description", "price", "quantity"}
        if not required_keys.issubset(data.keys()):
            raise ValueError("Словарь должен содержать ключи: 'name', 'description', 'price', 'quantity'")
        return cls(data["name"], data["description"], data["price"], data["quantity"])

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

    def __eq__(self, other):
        """Сравнение продуктов по названию и описанию."""
        if isinstance(other, Product):
            return self.name == other.name and self.description == other.description
        return False

    def __add__(self, other):
        """Сложение продуктов с возвратом общей стоимости."""
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Можно складывать только объекты Product")
