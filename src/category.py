class Category:
    """
    Класс, представляющий категорию товаров.
    """

    # Атрибуты класса для подсчета количества категорий и уникальных продуктов
    category_count = 0
    product_count = 0
    _unique_products = set()

    def __init__(self, name, description, products):
        """
        Инициализация категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов в категории
        """
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счетчик категорий
        Category.category_count += 1

        # Добавляем продукты в множество уникальных продуктов
        for product in products:
            Category._unique_products.add(product)

        # Обновляем счетчик уникальных продуктов
        Category.product_count = len(Category._unique_products)

    def __str__(self):
        """
        Возвращает строковое представление категории.
        """
        return f"{self.name}, Остаток: {len(self.products)} шт."

    def __repr__(self):
        return f"Category(name={self.name}, products={self.products})"
