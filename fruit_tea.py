"""
File: fruit_tea.py
Description: Defines the Topping class.
Author: Yu Song
ID: 110440805
Username: YUYSY041
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Bubble_tea import Bubble_tea


class Fruit_tea(Bubble_tea):
    # create attributes common
    def __init__(self, name, size, ice_level, sugar_level, tea_type, fruit, toppings=None):
        super().__init__(name, size, ice_level, sugar_level, tea_type, toppings)
        self.__fruit = fruit

    def calculate_price(self):
        size_cost = 0.85 if self.size == 'Medium' else 1.2 if self.size == 'Large' else 0
        fruit_cost = {'Mango': 0.3, 'Lychee': 0.1, 'Apple': 0.2, 'Grape': 0.4, 'Melon': 0.5, 'Grapefruit': 0.1,
                      'Lemon': 0.3, 'Guava': 0.2, 'Passionfruit': 0.25, 'Strawberry': 0.2, 'Pomegranate': 0.45,
                      'Peach': 0.1, 'Tropical': 0.65, 'Watermelon': 0.35}.get(self.__fruit, 0)
        toppings_cost = sum([topping.price for topping in self.toppings])
        return Bubble_tea.base_price + size_cost + fruit_cost + toppings_cost

    def __str__(self):
        return super().__str__() + f", Fruit: {self.__fruit}"
