"""Lists

Unique Sorted Sublists
Given a list of lists:
data = [[3, 1, 4], [1, 5, 9], [2, 6, 5], [3, 1, 4]]
Write a function that returns a new list containing only the unique sublists, each sorted in ascending order. Preserve the original order of first appearance.
Flatten and Remove Duplicates
Given a nested list (can have multiple levels):
nested = [1, [2, [3, 4], 5], 6, [7, 8, [9, 10]]]
Write a function to flatten it into a single list and remove all duplicates while maintaining the order of first appearance."""
from mesonbuild.interpreterbase import flatten

data = [[3, 1, 4], [1, 5, 9], [2, 6, 5], [3, 1, 4]]
# my_d =[[j for j in i if i[j]!=i[j+1]] for i in data ]
# print(my_d)
data.sort()
L=[j for m in data for j in m]
print(L)
unique_list = []
sol= [unique_list.append(x) for x in L if x not in unique_list]
print(sol)
unique_list = []

for item in L:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)

nested = [1, [2, [3, 4], 5], 6, [7, 8, [9, 10]]]
flat = flatten(nested)
    # [n for m in nested for n in m]
print(flat)
