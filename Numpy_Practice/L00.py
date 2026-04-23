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