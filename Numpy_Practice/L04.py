"""Dictionary → Normalized NumPy Array

Given a dictionary of values, convert it to a NumPy array and normalize it (min-max scaling).

# Input: {'a': 10, 'b': 20, 'c': 30}
# Output: array([0.0, 0.5, 1.0])"""
from collections import defaultdict

import numpy as np
from numpy import *


my_d={'a': 10, 'b': 20, 'c': 30}
my_arr=np.array(list(my_d.values()))
my_arr1=np.array(list(my_d.keys()))
print(my_arr,my_arr1)
arr=np.array([list(my_d.keys()), list(my_d.values())])
print(arr)
max_val=np.max(my_arr)
print(max_val)
min_val=np.min(my_arr)
print(min_val)
val=max_val-min_val
normal_l=[((each-min_val)/val) for each in my_arr]
print(list(normal_l))

"""Merge Lists with Different Lengths

Given two lists, convert to NumPy arrays and pad the shorter one with zeros before element-wise addition.

# Input: [1,2,3], [4,5]
# Output: [5,7,3]"""
import builtins
L1=[1,2,3]
L2=[4,5]
arr=np.array(L1)
arr1=np.array(L2)
max_len = builtins.max(len(L1), len(L2))
L1 += [0] * (max_len - len(L1))
L2 += [0] * (max_len - len(L2))

arr3 = np.array(L1) + np.array(L2)

print(arr3)


"""Set-Based Filtering with NumPy

Remove elements from a NumPy array that are present in a given exclusion set.

# Input: array([1,2,3,4,5]), exclude={2,4}
# Output: [1,3,5]"""

arr4= np.array([1,2,3,4,5])
exclude={2,4}
result = [x for x in arr4 if x not in exclude]
print(list(result))
print(arr4[~np.isin(arr4, exclude)])


"""Tuple Pair Transformation

Given a list of tuples, convert into a NumPy array and compute sum of each tuple.

# Input: [(1,2), (3,4), (5,6)]
# Output: [3,7,11]"""

L=np.array([(1,2), (3,4), (5,6)])
print(L)
res=[(i,(i[0]+i[1])) for i in L]
print(list(res))

"""Dictionary of Lists → Matrix

Convert a dictionary of lists into a 2D NumPy array.

# Input: {'a':[1,2], 'b':[3,4], 'c':[5,6]}
# Output:
# [[1,2],
#  [3,4],
#  [5,6]]"""
my_dict= {'a':[1,2], 'b':[3,4], 'c':[5,6]}
my_arr=np.array(list(my_dict.values()))
print(my_arr)


"""Unique Sorted Elements from Mixed Structures

Combine multiple lists, remove duplicates using set, and return sorted NumPy array.

# Input: [3,1,2], [2,4], [5,1]
# Output: [1,2,3,4,5]"""
L1=[3,1,2]
L2=[2,4]
L3=[5,1]
L=L1+L2+L3
print(L)
my_l=set(L)
res=np.array(list(set(L)))
print(res)
result = np.array(list(dict.fromkeys(L)))
print('ree',result)

"""Column-wise Dictionary Aggregation

Given a dict of lists, compute mean of each column using NumPy.

# Input: {'a':[1,2,3], 'b':[4,5,6]}
# Output: {'a_mean':2.0, 'b_mean':5.0}"""

d= {'a':[1,2,3], 'b':[4,5,6]}
ar=np.array( {'a':[1,2,3], 'b':[4,5,6]})
d1={(k+'_mean'):float(mean(v)) for k,v in d.items()}
print(d1)

"""Filter Tuples Based on Condition

From list of tuples, keep only those whose sum > threshold.

# Input: [(1,2),(3,4),(5,1)], threshold=5
# Output: [(3,4),(5,1)]"""
L=[(1,2),(3,4),(5,1)]
threshold=5
my_L=[i for i in L if i[0]+i[1]>threshold]
print(my_L)

"""Flatten + Frequency Mapping

Flatten a nested list, convert to NumPy array, and return frequency dictionary.

# Input: [[1,2],[2,3],[3,3]]
# Output: {1:1, 2:2, 3:3}"""

L=[[1,2],[2,3],[3,3]]
flat_l=[j for i in L for j in i]
a=np.array(L)
flat_a=np.array(flat_l)
print(a)
print(flat_a)
occ=defaultdict(int)
for i in flat_a:
    occ[int(i)]+=1
print(dict(occ))
flat=np.array(L).flatten()
values, counts = np.unique(flat, return_counts=True)
print(dict(zip(values,counts)))


"""Boolean Mask from Set

Create a boolean NumPy mask based on membership in a set.

# Input: array([1,2,3,4]), allowed={1,4}
# Output: [True, False, False, True]"""
import numpy as np

L = np.array([1, 2, 3, 4])
allowed = {1, 4}

mask = np.isin(L, list(allowed))

print("Mask:", mask)
print("Allowed values:", L[mask])
print("Excluded values:", L[~mask])

"""Dictionary Key Filtering + Array Conversion

Keep only dict values whose keys satisfy a condition, then convert to array.

# Input: {'a':10,'bb':20,'ccc':30}, keep keys len>1
# Output: [20,30]"""

ddd={'a':10,'bb':20,'ccc':30}
my_di=defaultdict(list)
for k,v in ddd.items():
    if len(k)>1:
        my_di[k].append(v)
print(np.array(list(my_di.values())))


"""Row-wise Tuple Sum Matrix

Convert list of tuples into matrix and compute row sums.

# Input: [(1,2,3),(4,5,6)]
# Output: [6,15]"""

T2=[(1,2,3),(4,5,6)]
my_t=defaultdict(int)

res=[]
for each in T2:
    sum=0
    for i in each:
        sum+=i
    res.append(sum)
print(res)
arr_t2=np.array(T2)
esults=np.sum(arr_t2,axis=1)
print(esults)

"""Merge & Deduplicate Multiple Sources

Merge lists + tuple + dict values into one unique NumPy array.

# Input: [1,2], (2,3), {'a':3,'b':4}
# Output: [1,2,3,4]"""

l=[1,2]
t=(2,3)
dts={'a':3,'b':4}
t_list=list(t)
dts_list=list(dts.values())
my_list=l+t_list+dts_list
my_set=set(my_list)
print(my_set)
print(my_list)
arr=np.array(list(my_set))
print(arr)

"""Sliding Window Sum

Compute sliding window sum on NumPy array.

# Input: [1,2,3,4,5], window=3
# Output: [6,9,12]
15. Dictionary Vector Dot Product

Given two dictionaries with same keys, treat values as vectors and compute dot product.

# Input: {'a':1,'b':2}, {'a':3,'b':4}
# Output: 11"""

L=[1,2,3,4,5]
window=3
ress=[]
ress1=[]
for each in range(len(L)-window+1):
    arr=np.array(L[each:each+window])
    arr_aum=np.sum(L[each:each+window])
    ress.append(arr)
    ress1.append(int(arr_aum))
print(ress,ress1)

d1={'a':1,'b':2}
d2={'a':3,'b':4}
val1=np.array(list(d1.values()))
val2=np.array(list(d2.values()))
print(np.dot(val1,val2))














