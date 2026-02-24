#1:
def square_generator(n):
    # Loop from 0 to n (inclusive)
    for i in range(n + 1):
        yield i * i   # yield returns one value at a time


# Test
n = int(input("Enter N: "))
for num in square_generator(n):
    print(num)


#2:
def even_numbers(n):
    for i in range(0, n+1, 2):
        yield str(i)

n = int(input())
first = True
# This is used to control comma printing.
# We don’t want a comma before the first number.
for i in even_numbers(n):
    if not first:
        print(",", end = "")
        #If it’s not the first number → print a comma.
    print(i, end = "")
    first = False
    

#3:
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input("Enter n: "))

for num in divisible_by_3_and_4(n):
    print(num)


#4:
def squares(a, b):
    # Loop from a to b (inclusive)
    for i in range(a, b + 1):
        yield i * i


# Test
a = int(input("Enter a: "))
b = int(input("Enter b: "))

for value in squares(a, b):
    print(value)
    
#5:
def countdown(n):
    # Continue while n is greater or equal to 0
    while n >= 0:
        yield n   # return current number
        n -= 1    # decrease n by 1


n = int(input("Enter n: "))

for num in countdown(n):
    print(num)