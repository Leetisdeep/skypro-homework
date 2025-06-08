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
        :param quantity: Количество на складе
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """
        Возвращает строковое представление продукта.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"

    def __add__(self, other):
        """
        Сложение двух продуктов по формуле: цена1 * количество1 + цена2 * количество2.
        
        :param other: Другой объект Product для сложения
        :return: Суммарная стоимость продуктов
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")
        
        return self.price * self.quantity + other.price * other.quantity


# Пример использования
if __name__ == "__main__":
    # Создаем продукты
    product_a = Product("Товар A", "Описание A", 100, 10)
    product_b = Product("Товар B", "Описание B", 200, 2)
    
    # Складываем продукты
    total_value = product_a + product_b
    
    print(product_a)  # Товар A, 100 руб. Остаток: 10 шт.
    print(product_b)  # Товар B, 200 руб. Остаток: 2 шт.
    print(f"Общая стоимость товаров: {total_value} руб.")  # Общая стоимость товаров: 1400 руб.
    
    # Создаем категорию с этими продуктами
    category = Category("Категория 1", "Описание категории", [product_a, product_b])
    
    print(category)  # Категория 1. Остаток: 2 шт.
    print(f"Всего категорий: {Category.category_count}")  # Всего категорий: 1
    print(f"Всего уникальных продуктов: {Category.product_count}")  # Всего уникальных продуктов: 2
