class Category:
    total_products = 0  # Класс-атрибут для подсчета продуктов

    def __init__(self):
        self.__products = []  # Приватный атрибут для хранения товаров

    def add_product(self, product):
        """Добавление продукта в категорию."""
        if isinstance(product, Product):
            for existing_product in self.__products:
                if existing_product.name == product.name:
                    # Объединяем количество
                    existing_product.quantity += product.quantity
                    # Выбираем более высокую цену
                    existing_product.price = max(existing_product.price, product.price)
                    return
            # Если дубликата нет, добавляем новый продукт
            self.__products.append(product)
            Category.total_products += 1  # Увеличиваем счетчик продуктов
        else:
            raise ValueError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        """Геттер для вывода списка товаров."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    @classmethod
    def new_product(cls, data):
        """Создание нового продукта из словаря."""
        if not isinstance(data, dict):
            raise ValueError("Данные должны быть переданы в виде словаря")
        required_keys = {"name", "price", "quantity"}
        if not required_keys.issubset(data.keys()):
            raise ValueError("Словарь должен содержать ключи: 'name', 'price', 'quantity'")
        return cls(data["name"], data["price"], data["quantity"])

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
