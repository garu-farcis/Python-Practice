"""Write a program to determine how many zeroes 1000! ends with."""

import math
s = str(math.factorial(1000))
print(s)
count = len(s) - len(s.rstrip('0'))

print(count)