import unittest
from discount_strategies import PercentageDiscount, BuyOneGetOneFree

class TestDiscountStrategies(unittest.TestCase):

    def test_percentage_discount(self):
        percentage_discount = PercentageDiscount(20)  # this is at 20% discount

        discounted_price = percentage_discount.apply_discount(100)
        self.assertEqual(discounted_price, 80)  # this is at 20% off on actual

    def test_buy_one_get_one_free(self):
        buy_one_get_one_free = BuyOneGetOneFree()

        discounted_price = buy_one_get_one_free.apply_discount(50)
        self.assertEqual(discounted_price, 25)  # this is offer buy one, get one free

if __name__ == "__main__":
    unittest.main()
