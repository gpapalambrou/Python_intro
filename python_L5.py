"""
Lesson 5: Libraries and Frameworks for Engineering Applications
Example Code: Using Numpy and Matplotlib

File: python_L5.py
GP, 26/2/25
"""

import numpy as np
import matplotlib.pyplot as plt

# Using Numpy for numerical operations
array = np.array([1, 2, 3, 4, 5])
squared_array = np.square(array)
print("Original array:", array)
print("Squared array:", squared_array)

# Using Matplotlib for data visualization
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Sine Wave")
plt.show()
