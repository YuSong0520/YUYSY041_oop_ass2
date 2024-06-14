"""
File: milk_tea.py
Description: Defines the Topping class.
Author: Yu Song
ID: 110440805
Username: YUYSY041
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Bubble_tea import Bubble_tea


class Milk_tea(Bubble_tea):
    # create attributes common
    def __init__(self, name, size, ice_level, sugar_level, tea_type, flavour, toppings=None):
        super().__init__(name, size, ice_level, sugar_level, tea_type, toppings)
        self.__flavour = flavour

    def calculate_price(self):
        size_cost = 0.85 if self.size == 'Medium' else 1.2 if self.size == 'Large' else 0
        flavour_cost = {'Mint Choc': 0.3, 'Thai': 0.35, 'Salted Caramel': 0.2, 'Roasted': 0.4, 'Earl Grey': 0.5,
                        'Vanilla': 0.1, 'Assam': 0.3, 'Hazelnut': 0.2, 'Oolong': 0.25, 'Jasmine': 0.2, 'Matcha': 0.45,
                        'Premium': 0.1, 'Taro': 0.65, 'Chocolate': 0.4}.get(self.__flavour, 0)
        toppings_cost = sum([topping.price for topping in self.toppings])
        return Bubble_tea.base_price + size_cost + flavour_cost + toppings_cost

    def __str__(self):
        return super().__str__() + f", Flavour: {self.__flavour}"
