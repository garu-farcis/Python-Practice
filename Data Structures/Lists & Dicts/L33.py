"""implement a function that takes two sorted lists and
returns a new sorted list containing the median of every pair of
corresponding elements after merging the two lists into one sorted sequence (handle odd/even lengths properly).
Sample Input: [1, 3, 5] and [2, 4, 6]
Sample Output: [1.5, 2.5, 3.5, 4.5, 5.5]"""
from statistics import median

a =[1, 3, 5]
b=[2, 4, 6]
c=sorted(a+b)
print(c)
med=[median([c[i], c[i + 1]])
    for i in range(len(c) - 1)]

print(med)
