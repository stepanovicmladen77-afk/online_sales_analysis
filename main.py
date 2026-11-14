import random
from product import Product
from product_manager import ProductManager
from cart import Cart

if __name__ == "__main__":
    manager = ProductManager()

    # Dodajemo nekoliko proizvoda u menadžer
    p1 = Product("Laptop", 85000.0, 5)
    p2 = Product("Miš", 2500.0, 15)
    p3 = Product("Tastatura", 4500.0, 10)
    
    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    # Kreirati instancu klase Cart
    cart = Cart()

    # Nasumično izabrati tri proizvoda iz liste dostupnih proizvoda instance ProductManager
    random_products = random.sample(manager.products, 3)
    for product in random_products:
        cart.add_to_cart(product, 1)

    # Ispisati ukupnu vrednost za naplatu sadržaja korpe, kao i proizvode koji se u njoj nalaze
    cart.display_cart()
    print(f"Ukupno za naplatu: {cart.calculate_total()} RSD")