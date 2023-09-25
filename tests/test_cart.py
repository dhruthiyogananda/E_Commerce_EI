import unittest
from products import Laptop, Headphones
from cart import Cart

class TestCart(unittest.TestCase):

    def test_add_to_cart(self):
        cart = Cart()
        laptop = Laptop("Laptop", 1000, True)
        cart.add_to_cart(laptop, 2)
        
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0].quantity, 2)
        self.assertEqual(cart.items[0].price, 1000)  # this is when no discount applied

    def test_remove_from_cart(self):
        cart = Cart()
        laptop = Laptop("Laptop", 1000, True)
        headphones = Headphones("Headphones", 50, True)

        cart.add_to_cart(laptop, 2)
        cart.add_to_cart(headphones)
        
        cart.remove_from_cart("Laptop")
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0].name, "Headphones")

    def test_update_quantity(self):
        cart = Cart()
        laptop = Laptop("Laptop", 1000, True)
        cart.add_to_cart(laptop, 2)

        cart.update_quantity("Laptop", 3)
        self.assertEqual(cart.items[0].quantity, 3)

    def test_calculate_total(self):
        cart = Cart()
        laptop = Laptop("Laptop", 1000, True)
        headphones = Headphones("Headphones", 50, True)

        cart.add_to_cart(laptop, 2)
        cart.add_to_cart(headphones)

        total = cart.calculate_total()
        self.assertEqual(total, 2050)  # this total includes 2 laptops and 1 headphone

if __name__ == "__main__":
    unittest.main()
