#1:
# Using Python built-in math functions

numbers = [5, -3, 12, 0, -7]

# Find the minimum value
print("Minimum:", min(numbers))  # Output: -7

# Find the maximum value
print("Maximum:", max(numbers))  # Output: 12


#2:
numbers = [5, -3, 12, 0, -7]
print("Absolute of -7:", abs(-7))  # Output: 7

# Round a floating number
print("Round 3.7:", round(3.7))  # Output: 4
print("Round 3.2:", round(3.2))  # Output: 3

# Power function: 2 raised to 3
print("2 to the power of 3:", pow(2, 3))  # Output: 8


#3:
import math  # Import math module for more advanced functions

# Square root of 16
print("Square root of 16:", math.sqrt(16))  # Output: 4.0

# Ceiling (round up) and floor (round down)
print("Ceil of 3.2:", math.ceil(3.2))   # Output: 4
print("Floor of 3.8:", math.floor(3.8)) # Output: 3

# Trigonometric functions (angle in radians)
angle = math.pi / 2  # 90 degrees in radians
print("Sin(pi/2):", math.sin(angle))  # Output: 1.0
print("Cos(pi/2):", math.cos(angle))  # Output: 0.0

# Constants
print("Value of pi:", math.pi)  # Output: 3.141592653589793
print("Value of e:", math.e)    # Output: 2.718281828459045


#4:
import random  # Import random module

# Random integer between 1 and 10
print("Random integer 1-10:", random.randint(1, 10))  # Example: 7

# Random choice from a list
colors = ["red", "blue", "green", "yellow"]
print("Random color:", random.choice(colors))  # Example: blue