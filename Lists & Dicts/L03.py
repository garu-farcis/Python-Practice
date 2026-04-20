"""Dictionaries

Merge Dictionaries with Priority
You have two dictionaries:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
Merge them such that if a key exists in both, the value from dict2 takes priority. Return the merged dictionary.
Group by First Letter
Given a list of words:
words = ["apple", "banana", "avocado", "blueberry", "cherry", "date"]
Create a dictionary where the keys are the first letters (lowercase) and the values are lists of words starting with that letter.
Invert Dictionary (Handle Duplicates)
Given a dictionary:
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 85, 'David': 78}
Invert it so that keys become values and values become keys. If multiple keys have the same value, store them in a list as the new value."""

from itertools import groupby
from collections import defaultdict
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
d = defaultdict(list)

for dct in (dict1, dict2):
    if 'c' in dct:
        d['c'].append(dct['c'])

print(d)
dict1.update(dict2)
print(dict1)
L =list(dict1)
print(L)

words = ["apple", "banana", "avocado", "blueberry", "cherry", "date"]
ans = { i[0].lower():[v for v in words if v[0]==i[0]]for i in words}
print(ans)

scores = {'Alice': 85, 'Bob': 92, 'Charlie': 85, 'David': 78}
my_dict={v:[k if scores[k]>1 else scores[k]] for k,v in scores.items()}
print(my_dict)
d1 =defaultdict(list)
for k,v in scores.items():
    d1[v].append(k)
print(d1)