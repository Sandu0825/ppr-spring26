# This program demonstrates map(), filter(), and reduce()
#functools is a Python module with special tools for working with functions.
from functools import reduce

numbers = [1, 2, 3, 4, 5]

#map() applies a function to every element
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

#filter() keeps only elements that satisfy a condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#reduce() combine into one value,combines all values into one result
sum_numbers = reduce(lambda a, b: a + b, numbers)
print("Sum using reduce:", sum_numbers)