from src.product import Product

class Category:
    """Класс категории товаров"""

    all_category = 0
    all_products = 0  

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = []

        Category.all_category += 1
        
        for product in products:
            self.add_product(product)

    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)
    
    def get_products_list(self) -> list:
        """Вспомогательный метод для получения списка продуктов"""
        return self.__products

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )
        
        # Проверка на дубликаты (по имени)
        for existing_product in self.__products:
            if existing_product.name == product.name:
                # Если продукт уже есть, увеличиваем количество
                existing_product.quantity += product.quantity
                return
                
        # Если продукта нет в списке, добавляем его
        self.__products.append(product)
        Category.all_products += 1  # Увеличиваем только для уникальных продуктов

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def average_price(self) -> float:
        """Метод расчета средней цены товаров в категории"""
        if not self.__products:
            return 0

        try:
            total = sum(product.price for product in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0
