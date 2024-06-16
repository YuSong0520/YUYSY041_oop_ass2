"""
File: store.py
Description: Defines the Store class.
Author: Your Name
ID: Your ID
Username: yourusername
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from fruit_tea import Fruit_tea
from milk_tea import Milk_tea
from sparkling_tea import Sparkling_tea
from hot_tea import Hot_tea
from frozen_tea import Frozen_tea
from topping import Topping


class Store:
    def __init__(self):
        self.__orders = []
        self.__earnings = 0.0

    def order_tea(self, tea):
        self.__orders.append(tea)
        self.__earnings += tea.calculate_price()

    def show_order_history(self):
        for tea in self.__orders:
            print(tea)

    @property
    def earnings(self):
        return self.__earnings

    def __str__(self):
        return f"Total earnings: ${self.__earnings:.2f}"


# example for ordering
if __name__ == "__main__":
    store = Store()

    # Ordering different teas and choose different things
    fruit_tea = Fruit_tea("Fruit Tea", "Medium", "Normal", "Full", "Green", "Mango",
                          [Topping("Pearls", 1.2), Topping("Aloe Vera", 0.7)])
    store.order_tea(fruit_tea)

    milk_tea = Milk_tea("Milk Tea", "Large", "Less", "Half", "Black", "Earl Grey", [Topping("Mousse", 2.4)])
    store.order_tea(milk_tea)

    sparkling_tea = Sparkling_tea("Sparkling Tea", "Small", "Normal", "Full", "Green", [Topping("Cookie Crumb", 0.75)])
    store.order_tea(sparkling_tea)

    hot_tea = Hot_tea("Hot Tea", "Large", "None", "Full", "Black", [Topping("Mixed Jellies", 0.35)])
    store.order_tea(hot_tea)

    frozen_tea = Frozen_tea("Frozen Tea", "Large", "Normal", "Half", "Green", True, True,
                            [Topping("Herbal Jelly", 0.45), Topping("Mango Popping Pearls", 0.4)])
    store.order_tea(frozen_tea)

    store.show_order_history()
    print(store)
