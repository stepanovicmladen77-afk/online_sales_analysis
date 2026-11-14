class ProductManager:
    def __init__(self):
        self.products = []  # Lista u kojoj čuvamo proizvode

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            print(f"Proizvod: {product.name}, Cena: {product.price}, Količina: {product.quantity}")