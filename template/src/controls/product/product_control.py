
from data.manager.product_manager import ProductManager

class ProductControl:
    def __init__(self):
        self.manager = ProductManager()

    def get_all_products(self):
        return self.manager.get_all_products()

    def create_product(self, name, code, price, image):
        return self.manager.create_product(code, name, price, image)