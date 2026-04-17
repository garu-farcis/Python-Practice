"""
1.Rewrite question 5 using a list comprehension (squares from 1 to 10). Then do the same for cubes using a one-line list comprehension.
2.Using a list comprehension, create a list positive from numbers = [-5, -3, 0, 2, 4, -1, 7] that contains only the positive numbers (> 0).
3.Using a dictionary comprehension, create a dict square_dict where the keys are numbers 1 to 10 and the values are their squares.
4.Given two lists:

Pythonnames = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
Create a dictionary people using a dictionary comprehension + zip().

5.Predict the output:

Pythonresult = {x: x**2 for x in range(5) if x % 2 == 0}
print(result)

6. Given a list of tuples:

Pythonpairs = [("a", 1), ("b", 2), ("c", 3), ("a", 4)]
Convert it into a dictionary where duplicate keys keep the last value (use dict()).

7. Convert the dictionary from question 16 back into a list of tuples using .items().
8. Given words = ["hello", "world", "python", "code"], use a list comprehension to create a new list containing only the words with length > 4, converted to uppercase.
9. Using a dictionary comprehension, create a dict that counts the frequency of each character in the string s = "banana".
10. Given scores = {"Alice": 85, "Bob": 92, "Charlie": 78}, write a dictionary comprehension to
 create a new dict passed that contains only students with score ≥ 80, and add 5 bonus points to each value."""

L = [i**3 for i in range(1,11)]
print(L)

L1 =[-5, -3, 0, 2, 4, -1, 7]
print(L1)
L2=[i for i in L1 if i>=0]
print(L2)

my_dict={i:i**2 for i in range(1,11)}
print(my_dict)

p =['alice','bob','charlie']
ages = [25, 30, 35]
print(dict(zip(p,ages)))


result = {x: x**2 for x in range(5) if x % 2 == 0}
print(result)

e =[('a', 1), ('b', 2), ('c', 3), ('a', 4)]
print(dict(e))

from collections import defaultdict

pairs = [("a", 1), ("b", 2), ("c", 3), ("a", 4)]

result = defaultdict(list)

for key, value in pairs:
    result[key].append(value)

print(dict(result))


words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

count = defaultdict(int)

for word in words:
    count[word] += 1        # No KeyError!

print(dict(count))


def func1(x):
    x = x + 1
    return x
def func2(L):
    L = L + [1]
    return L
a=3
M=[1,2,3]
print(func1(a))
print(func2(M))