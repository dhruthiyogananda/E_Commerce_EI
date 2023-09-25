from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, price):
        return price * (1 - self.percentage / 100)

class BuyOneGetOneFree(DiscountStrategy):
    def apply_discount(self, price):
        return price / 2
