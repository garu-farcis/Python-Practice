"""Tuples
Group Tuples by Second Element
Given:
data = [('a', 1), ('b', 2), ('c', 1), ('d', 2), ('e', 3)]
Group tuples into a dictionary where the key is the second element, and the value is a list of first elements.
Find Pair with Maximum Sum
Given a list of tuples:
pairs = [(1, 5), (3, 7), (2, 9), (4, 6)]
Find the tuple with the maximum sum of its elements."""
from collections import defaultdict
data = [('a', 1), ('b', 2), ('c', 1), ('d', 2), ('e', 3)]
my_dict={v:k for k,v in set(data)}
print(my_dict)
d= defaultdict(list)
for k,v in data:
    d[v].append(k)
print(d)
myd= [sorted(data,key=lambda x:x[1])]
print(myd)

pairs = [(1, 5), (3, 7), (2, 9), (4, 6)]
res= sorted(pairs,key=lambda x:x[0]+x[1],reverse = True)
print(res)
print(res[0])