"""Sets

Find Missing Numbers Using Sets
Given a list nums = [1, 2, 4, 6, 8, 9] and a range from 1 to 10, find all numbers missing from the list using sets.
Set Operations on Multiple Sets
You have three sets:
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {5, 6, 7, 8}
Find elements that appear in exactly two of the three sets.
Remove Elements from List Using Set
Given:
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_set = {3, 6, 9}
Remove all elements present in remove_set from original while preserving the order of remaining elements.
Do not use list comprehension with if condition — use set for O(1) lookup."""

nums = [1, 2, 4, 6, 8, 9]
missing_nums=[]
for i in range(1,11):
    if i not in nums:
        missing_nums.append(i)
print(missing_nums)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {5, 6, 7, 8}
element=(
    (s1 & s2) |
    (s2 & s3) |
    (s1 & s3)
) - (s1 & s2 & s3)

print(element)

s = [j for i in (s1,s2,s3) for j in i]
print(s)
e = list(element)
print(e)
L=[]
for i in s:
    if i not in e:
        L.append(i)
print('new list', L)
