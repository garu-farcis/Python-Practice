"""1. Remove Duplicates (Preserve Order)

Write a function that removes duplicates from a list while keeping the original order.

# Input: [1, 2, 2, 3, 1, 4]
# Output: [1, 2, 3, 4]"""

L = [1, 2, 2, 3, 1, 4]
unique_list=[]
for i in L:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

"""Two Sum (All Pairs)

Return all unique pairs of numbers that sum to a target.

# Input: nums = [2, 4, 3, 5, 7, -1], target = 6
# Output: [(2,4), (3,3?) no if only one 3, (7,-1)]"""

nums = [2, 4, 3, 5, 7, -1]
print(nums)
target = 6
L1=[]
comp =[i for i in nums]
print(comp)
for each in range(len(nums)):
    for i in comp:
        if nums[each]+i ==target:
            L1.append((i,nums[each]))
print('my tuples', L1)


"""Frequency Counter

Count how many times each element appears.

# Input: ['a', 'b', 'a', 'c', 'b', 'a']
# Output: {'a': 3, 'b': 2, 'c': 1}"""

L =['a', 'b', 'a', 'c', 'b', 'a']
freq={}
for i in L:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)


"""Merge Dictionaries

Merge two dictionaries. If keys overlap, sum their values.

# Input: {'a': 2, 'b': 3}, {'b': 4, 'c': 5}
# Output: {'a': 2, 'b': 7, 'c': 5}"""
from collections import ChainMap
from collections import defaultdict
my_dict = {'a': 2, 'b': 3}
my_dict1={'b': 4, 'c': 5}
dct=ChainMap(my_dict,my_dict1)
print(dct.maps)
new_dct= defaultdict(int)
for i in dct.maps:
    for k,v in i.items():
        new_dct[k]+=v
print(dict(new_dct))


"""Invert Dictionary

Swap keys and values. If duplicate values exist, store keys in a list.

# Input: {'a': 1, 'b': 2, 'c': 1}
# Output: {1: ['a','c'], 2: ['b']}"""

dd={'a': 1, 'b': 2, 'c': 1}
defa=defaultdict(list)
for k,v in dd.items():
    defa[v].append(k)
print(dict(defa))

"""Set Intersection & Difference

Return both intersection and difference of two lists.

# Input: [1,2,3,4], [3,4,5,6]
# Output: ([3,4], [1,2])"""

a=[1,2,3,4]
b=[3,4,5,6]
a1=set(a)
b1=set(b)
print(a1&b1)
print(a1-b1)

"""Tuple Unpacking Challenge

Given a list of tuples, extract elements into separate lists.

# Input: [(1,'a'), (2,'b'), (3,'c')]
# Output: [1,2,3], ['a','b','c']"""
x = [(1,'a'), (2,'b'), (3,'c')]
c1=[]
d1=[]


for i in x:
    if isinstance(i,tuple):
        c1.append(i[0])
        d1.append(i[1])
print(c1)
print(d1)

"""Second Largest Element

Find the second largest number without sorting the entire list.

# Input: [10, 20, 4, 45, 99]
# Output: 45"""

nums = [10, 5, 8, 20, 15]

largest = float('-inf')
second = float('-inf')

for num in nums:
    if num > largest:
        second = largest
        largest = num
    elif largest > num > second:
        second = num

print(second)