#exercise 1:
x = lambda a : a + 10
print(x(5))

#exercise 2:
x = lambda a, b : a * b
print(x(5, 6))

#exercise 3:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#exercise 4:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

