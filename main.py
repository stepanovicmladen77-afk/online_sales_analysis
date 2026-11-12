from product import Product
from product_manager import ProductManager
from cart import Cart

if __name__ == "__main__":
    manager = ProductManager()
    
    p1 = Product("Laptop", 85000.0, 5)
    p2 = Product("Miš", 2500.0, 15)
    p3 = Product("Tastatura", 4500.0, 10)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    # Kreirati instancu klase Cart
    cart = Cart()

    # U korpu dodati tri slučajno odabrana proizvoda iz liste dostupnih proizvoda instance ProductManager
    cart.add_to_cart(p1, 1)
    cart.add_to_cart(p2, 2)
    cart.add_to_cart(p3, 1)

    # Ispisati ukupnu vrednost za naplatu sadržaja korpe, kao i proizvode koji se u njoj nalaze
    cart.display_cart()
    print(f"\nUkupno za naplatu: {cart.calculate_total()} RSD")