#exercise 1:
def myfunc():
  x = 300
  print(x)

myfunc()

#exercise 2:
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

#exercise 3:
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#exercise 4:
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

