"""Sets

Intersection of Multiple Lists
Given a list of lists:
lists = [[1, 2, 3, 4], [2, 3, 5, 6], [3, 4, 7, 8], [3, 9, 10]]
Find the elements that are present in all the inner lists using sets.
Union Minus Intersection
Given two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
Compute the elements that are in exactly one of the sets (i.e., (union - intersection)).
Detect Duplicates in List of Tuples
Given a list of tuples:
transactions = [(101, 'buy'), (102, 'sell'), (101, 'buy'), (103, 'buy'), (102, 'sell')]
Use a set to detect and return only the duplicate tuples (tuples that appear more than once)."""

lists = [[1, 2, 3, 4], [2, 3, 5, 6], [3, 4, 7, 8], [3, 9, 10]]
res = set(lists[0]).intersection(*lists[1:])
print(list(res))
ele=[x for x in lists[0] if all(x in lists for lists in lists[1:])]
print(ele)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result = (set1 | set2)-(set1 & set2)
print(result)


transactions = [(101, 'buy'), (102, 'sell'), (101, 'buy'), (103, 'buy'), (102, 'sell')]
unique=[]
dup=[]
for each in transactions:
    if each not in unique:
        unique.append(each)
    else:
        dup.append(each)
print(unique,'hgdsgggfjs,k   ', dup)
