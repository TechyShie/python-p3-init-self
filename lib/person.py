#!/usr/bin/env python3

class Person:
    def __init__(self, name, height = "158cm"):
        self.name = name
        self.height = height 



John = Person("John")
print(John.name)