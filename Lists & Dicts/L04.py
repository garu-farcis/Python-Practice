"""Sets

Common Elements in Multiple Lists
Given three lists:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6, 7]
list3 = [1, 3, 5, 8]
Find the elements that are common to all three lists using sets.
Symmetric Difference of Sets
You have two sets:
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
Compute the symmetric difference and then convert the result into a sorted list.
Remove Duplicates while Preserving Order
Given a list with duplicates:
items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
Remove duplicates while preserving the original order of first appearance without using OrderedDict or dict.fromkeys() (use sets creatively)."""

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6, 7]
list3 = [1, 3, 5, 8]
ch= set(list1) & set(list2) & set(list3)
print('elements that are common to all three lists using sets', ch)

from collections import Counter

lists = [list1, list2, list3]
counter = Counter()

for lst in lists:
    counter.update(set(lst))
print(counter)

result = [x for x, c in counter.items() if c >= 2]
print(result)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
diff = set_a^set_b
print(list(diff))

items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
dups_out=[]
for i in items:
    if i not in dups_out:
        dups_out.append(i)
print(dups_out)