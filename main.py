from products import Laptop, Headphones
from discount_strategies import PercentageDiscount, BuyOneGetOneFree
from cart import Cart

if __name__ == "__main__":
    laptop = Laptop("Laptop", 1000, True)
    headphones = Headphones("Headphones", 50, True)

    cart = Cart()
    cart.add_to_cart(laptop, 2)
    cart.add_to_cart(headphones)
    print(cart)

    total_bill = cart.calculate_total()
    print(f"Your total bill is ${total_bill}.")
