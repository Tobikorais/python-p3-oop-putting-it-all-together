#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition="New"):
        self.brand = brand
        self.size = size
        self.condition = condition

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string.")
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        elif value <= 0:
            print("Size must be a positive number.")
        else:
            self._size = value

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value):
        if not isinstance(value, str):
            raise ValueError("Condition must be a string.")
        self._condition = value

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"