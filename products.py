class Product:
    def __init__(self, name, price, available):
        self.name = name
        self.price = price
        self.available = available

class Laptop(Product):
    pass

class Headphones(Product):
    pass
