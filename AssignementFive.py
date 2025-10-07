# Base class
class Smartphone:
    def __init__(self, model, brand, price):
        self.model = model
        self.brand = brand
        self.price = price

    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")

# Subclass
class Samsung(Smartphone):
    def __init__(self, model, brand, price, camera_megapixels):
        super().__init__(model, brand, price)
        self.camera_megapixels = camera_megapixels

    # Overriding method (polymorphism)
    def show_info(self):
        super().show_info()
        print(f"Camera: {self.camera_megapixels}MP")


# Example usage
phone1 = Samsung("Galaxy S23", "Samsung", 999.99, 108)
phone1.show_info()
