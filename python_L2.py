"""
Lesson 2: Control Structures and Functions
Example Code: Conditional Statements and Loops

File: python_L2.py
GP, 26/2/25
"""


# Conditional statements
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")

# For loop
for i in range(5):
    print("Iteration", i)

# While loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))
