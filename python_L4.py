"""
Lesson 4: Object-Oriented Programming (OOP)
Example Code: Classes and Objects

File: python_L4.py
GP, 26/2/25
"""

# Defining a class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object
my_dog = Dog("Buddy", "Golden Retriever")

# Calling a method
print(my_dog.bark())
