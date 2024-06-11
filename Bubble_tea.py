"""
File: topping.py
Description: Implements the Topping class and the abstract BubbleTea class.
Author: Yu Song
ID: 110440805
Username: YUYSY041
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from abc import ABC, abstractmethod


# Define an abstract base class for Bubble tea
class Bubble_tea(ABC):
    base_price = 4.5  # Base price for all bubble teas

    # Constructor to initialize attributes common to all bubble teas
    def __init__(self, name, size, ice_level, sugar_level, tea_type, toppings):
        self.name = name
        self.size = size
        self.ice_level = ice_level
        self.sugar_level = sugar_level
        self.tea_type = tea_type
        self.toppings = []  # Initialize an empty list for toppings

    # Method to add a topping to the bubble tea
    def add_topping(self, topping):
        self.toppings.append(topping)

    # Method to remove a topping from the bubble tea
    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)

    # Method to represent the bubble tea as a string
    def __str__(self):
        toppings_str = ", ".join(str(topping) for topping in self.toppings)
        return f"{self.name} ({self.size}, {self.ice_level} ice, {self.sugar_level} sugar, {self.tea_type}) with toppings: {toppings_str}"

    @abstractmethod
    def calculate_price(self):
        pass
