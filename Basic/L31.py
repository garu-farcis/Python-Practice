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

l = [x for i in range(11) for x in ([1] + [0]*i)]
print(l)