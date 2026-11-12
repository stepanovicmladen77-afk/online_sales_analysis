def remove_product_by_name(self, name: str):
        """Uklanjanje proizvoda prema imenu."""
        self.products = [p for p in self.products if p.name.lower() != name.lower()]