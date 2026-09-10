""". Given two lists of integers, return a sorted list of all unique elements that appear in both lists (intersection) without using set operations directly on the lists.
Sample Input: [1, 3, 5, 7, 9, 3] and [3, 4, 5, 6, 7, 5]
Sample Output: [3, 5, 7]"""

a=[1, 3, 5, 7, 9, 3]
b= [3, 4, 5, 6, 7, 5]
sort_intersection=[i for i in a if i in b]
print(set(sort_intersection))