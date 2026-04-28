"""Create a find . -name "numpy.py"NumPy array from a Python list:

[1, 2, 3, 4, 5]
Then create a 2×3 array filled with zeros."""
import numpy as np
my_arr= np.array([1, 2, 3, 4, 5])
# a=np.reshape(my_arr,(2,3))
zeros_arr = np.zeros((2, 3))
print(zeros_arr)

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")

say_hello()

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())


def changecase(func):
  def myinner1(x):
    return func(x).upper()
  return myinner1

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)

  # List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

  # Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

import datetime

x = datetime.datetime.now()
x = datetime.datetime(2020, 5, 17)
print(x)
print(x.strftime("%B"))

y= datetime.date.today()
print(y)

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)
print(y)

# the result is a Python dictionary:
print(y["age"])

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
print(json.dumps(x, indent=4, separators=(". ", " = "),sort_keys=True))
txt = f"The price is 49 dollars"
print(txt)