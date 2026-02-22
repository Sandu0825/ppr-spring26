#1:
# We create a list
numbers = [1, 2, 3]

# Convert list into an iterator
my_iterator = iter(numbers)

# Get elements one by one using next()
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
#next() gets the next value.

# If we call next() again, it will give an error (StopIteration)


#2:
# Custom iterator that counts from 1 to n
class MyNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self  # returns the iterator object

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration  # stop when limit reached

# Create object
nums = MyNumbers(5)

# Loop through it
for number in nums:
    print(number)
    

#3:
# Generator that gives square numbers

def square_generator(n):
    for i in range(n):
        yield i * i  # returns value and pauses here


# Create generator object
gen = square_generator(5)

# Print values
for value in gen:
    print(value)

#4:
# Generator expression (like list comprehension but with parentheses)
#A generator expression is a short way to create a generator.
#It looks like a list comprehension — but uses parentheses () instead of square brackets []
#() creates one by one

gen = (x * 2 for x in range(5))

# Loop through generator
for value in gen:
    print(value)