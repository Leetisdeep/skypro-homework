class Category:
    """
    Класс, представляющий категорию товаров.
    """
    category_count = 0
    product_count = 0
    _unique_products = set()

    def __init__(self, name, description, products):
        """
        Инициализация категории.
        """
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут

        Category.category_count += 1
        for product in products:
            Category._unique_products.add(product)
        Category.product_count = len(Category._unique_products)

    @property
    def products(self):
        """Геттер для списка продуктов."""
        return self.__products

    def add_product(self, product):
        """Добавление продукта в категорию."""
        if isinstance(product, Product):
            for existing_product in self.__products:
                if existing_product == product:
                    existing_product.quantity += product.quantity
                    existing_product.price = max(existing_product.price, product.price)
                    return
            self.__products.append(product)
            Category._unique_products.add(product)
            Category.product_count = len(Category._unique_products)
        else:
            raise ValueError("Можно добавлять только объекты класса Product")

    def __str__(self):
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __repr__(self):
        return f"Category(name={self.name}, products={self.__products})"
