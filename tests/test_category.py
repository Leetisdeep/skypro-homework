class Category:
    category_count = 0
    product_count = 0
    _unique_products = set()  # Для хранения уникальных продуктов

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        # Увеличиваем счетчик категорий
        Category.category_count += 1

        # Добавляем продукты в множество уникальных продуктов
        if products:
            for product in products:
                if product not in Category._unique_products:
                    Category._unique_products.add(product)
                    Category.product_count += 1

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, value):
        self.__products = value
        # При обновлении списка продуктов также обновляем уникальные продукты
        for product in value:
            if product not in Category._unique_products:
                Category._unique_products.add(product)
                Category.product_count += 1

    def __del__(self):
        """Уменьшаем счетчики при удалении категории"""
        Category.category_count -= 1
        # Можно также уменьшить product_count, если нужно
