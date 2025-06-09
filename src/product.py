class Product:
    """
    Класс, представляющий продукт.
    """

    def __init__(self, name, description, price, quantity):
        """
        Инициализация продукта.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена продукта
        :param quantity: Количество продукта
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return (f"Product(name={self.name}, price={self.price}, "
                f"quantity={self.quantity})")

    def __str__(self):
        """
        Возвращает строковое представление продукта.
        """
        return (f"Продукт: {self.name}\n"
                f"Описание: {self.description}\n"
                f"Цена: {self.price} руб.\n"
                f"Количество: {self.quantity} шт.")

    def __eq__(self, other):
        """
        Сравнение двух продуктов по их атрибутам.
        """
        if isinstance(other, Product):
            return (self.name == other.name and
                    self.description == other.description and
                    self.price == other.price and
                    self.quantity == other.quantity)
        return False

    def __add__(self, other):
        """
        Сложение двух продуктов.
        Если продукты одинаковые (по названию, описанию и цене),
        складывается их количество.
        """
        if self == other:
            return Product(
                name=self.name,
                description=self.description,
                price=self.price,
                quantity=self.quantity + other.quantity
            )
        else:
            raise ValueError("Нельзя складывать разные продукты")

    def __hash__(self):
        """
        Хэширование продукта для использования в множествах.
        """
        return hash((self.name, self.description, self.price, self.quantity))
