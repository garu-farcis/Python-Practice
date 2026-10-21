"""Use a list comprehension to create the list below, which consists of ones separated by increasingly many zeroes.
The last two ones in the list should be separated by ten zeroes.
[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

[1,
 1,0,
 1,0,0,
 1,0,0,0,
 1,0,0,0,0,
 ...
]"""
from pprint import pprint

l = [x for i in range(11) for x in ([1] + [0]*i)]
print(l)
L = [[[0]*5 for i in range(5)] for j in range(5)]
pprint(L)