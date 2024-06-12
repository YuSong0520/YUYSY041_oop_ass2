"""
File: frozen_tea.py
Description: Defines the Topping class.
Author: Yu Song
ID: 110440805
Username: YUYSY041
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Bubble_tea import Bubble_tea


class Frozen_tea(Bubble_tea):
    # create attributes common to Frozen tea
    def __init__(self, name, size, ice_level, sugar_level, tea_type, fruity, milky, toppings=None):
        super().__init__(name, size, ice_level, sugar_level, tea_type, toppings)
        self.__fruity = fruity
        self.__milky = milky

    def calculate_price(self):
        # calculate the price
        size_cost = 0.85 if self.size == 'Medium' else 1.2 if self.size == 'Large' else 0
        fruity_cost = 0.15 if self.__fruity else 0
        milky_cost = 0.29 if self.__milky else 0
        toppings_cost = sum([topping.price for topping in self.toppings])
        return Bubble_tea.base_price + size_cost + fruity_cost + milky_cost + toppings_cost

    def __str__(self):
        return super().__str__() + f", Fruity: {self.__fruity}, Milky: {self.__milky}"
