class Product:
    def _init_(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        """Metod za prikaz informacija o proizvodu."""
        print(f"Proizvod: {self.name} | Cena: {self.price} RSD | Količina: {self.quantity}")

    def update_quantity(self, amount: int):
        """Metod za ažuriranje količine proizvoda."""
        self.quantity += amount
        if self.quantity < 0:
            self.quantity = 0