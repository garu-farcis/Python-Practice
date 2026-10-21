import random

s = input("enter a string: ")
chars = list(s)

random.shuffle(chars)

result = ''.join(chars)
print(result)