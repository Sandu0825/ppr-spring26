#exercise 1:
x = 5
y = "Alice"
print(x)
print(y)

#exercise 2:
x = str(10)    
y = int(10)    
z = float(10) 

#exercise 3:
#Legal variable names:

myvar = "HI"
my_var = "HI"
_my_var = "HI"
myVar = "HI"
MYVAR = "HI"
myvar2 = "HI"

#exercise 4:
x = y = z = "Apple"
print(x)
print(y)
print(z)

#exercise 5:
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)