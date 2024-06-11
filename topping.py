"""
File: topping.py
Description: Defines the Topping class.
Author: Yu Song
ID: 110440805
Username: YUYSY041
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Topping:
    # create attributes common topping
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property  # call the property method
    def price(self):
        return self.__price

    def __str__(self):
        return f"{self.__name} (${self.__price:.2f})"
