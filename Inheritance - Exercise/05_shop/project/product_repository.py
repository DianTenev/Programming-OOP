from typing import List, Optional

from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name) -> Optional[Product]:
        res = [p for p in self.products if p.name == product_name]
        if res:
            return res[0]

    def remove(self, product_name):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        info = "\n".join([f"{product.name}: {product.quantity}" for product in self.products])
        return info


