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
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

    def __eq__(self, other):
        """
        Сравнение двух продуктов по их атрибутам.
        """
        if isinstance(other, Product):
            return (
                self.name == other.name and
                self.description == other.description and
                self.price == other.price and
                self.quantity == other.quantity
            )
        return False

    def __hash__(self):
        """
        Хэширование продукта для использования в множествах.
        """
        return hash((self.name, self.description, self.price, self.quantity))
