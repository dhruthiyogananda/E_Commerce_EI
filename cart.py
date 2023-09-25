import copy

class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity=1, discount_strategy=None):
        # Clone the product and add it to the cart
        cloned_product = copy.deepcopy(product)
        cloned_product.quantity = quantity

        # Apply the discount strategy if provided
        if discount_strategy:
            cloned_product.price = discount_strategy.apply_discount(cloned_product.price)

        self.items.append(cloned_product)

    def remove_from_cart(self, product_name):
        self.items = [item for item in self.items if item.name != product_name]

    def update_quantity(self, product_name, new_quantity):
        for item in self.items:
            if item.name == product_name:
                item.quantity = new_quantity

    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.items)
        return total

    def __str__(self):
        item_counts = {}
        for item in self.items:
            item_counts[item.name] = item_counts.get(item.name, 0) + item.quantity
        cart_items = ", ".join([f"{count} {name}" for name, count in item_counts.items()])
        return f"You have {cart_items} in your cart."
