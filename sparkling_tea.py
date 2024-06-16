"""
File: sparking_tea.py
Description: Defines the Topping class.
Author: Yu Song
ID: 110440805
Username: YUYSY041
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Bubble_tea import Bubble_tea


class Sparkling_tea(Bubble_tea):
    def calculate_price(self):
        size_cost = 0.85 if self.size == 'Medium' else 1.2 if self.size == 'Large' else 0
        tea_type_cost = 0.19
        toppings_cost = sum([topping.price for topping in self.toppings])
        return Bubble_tea.base_price + size_cost + tea_type_cost + toppings_cost

    def __str__(self):
        return super().__str__()
