from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product: Product, quantity: int = 1):
        """Dodavanje proizvoda u korpu."""
        self.cart_items.append({"product": product, "quantity": quantity})

    def calculate_total(self) -> float:
        """Računanje ukupne vrednosti korpe, tj. iznosa za naplatu."""
        total = sum(item["product"].price * item["quantity"] for item in self.cart_items)
        return total

    def display_cart(self):
        """Prikaz sadržaja korpe."""
        print("--- SADRŽAJ KORPE ---")
        if not self.cart_items:
            print("Korpa je prazna.")
        for item in self.cart_items:
            p = item["product"]
            q = item["quantity"]
            print(f"- {p.name} | Količina: {q} | Cena po komadu: {p.price} RSD")