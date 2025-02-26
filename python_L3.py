"""
Lesson 3: Data Structures and Algorithms
Example Code: Lists and Sorting

File: python_L3.py
GP, 26/2/25
"""


# Creating and manipulating a list
numbers = [5, 2, 9, 1, 5, 6]
print("Original list:", numbers)

# Sorting the list
numbers.sort()
print("Sorted list:", numbers)

# Using a tuple
coordinates = (10, 20)
print("Coordinates:", coordinates)

# Using a dictionary
student = {"name": "Alice", "age": 23, "is_student": True}
print("Student info:", student)

# Searching for an element
target = 5
found = target in numbers
print("Is 5 in the list?", found)
