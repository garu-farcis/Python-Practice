"""Implement a function that takes a list of strings and returns a dictionary where keys are the unique
 first characters and values are sorted lists of all words starting with that character.
Sample Input: ["apple", "banana", "apricot", "blueberry", "avocado", "cherry"]
Sample Output: {"a": ["apple", "apricot", "avocado"], "b": ["banana", "blueberry"], "c": ["cherry"]}"""

from collections import defaultdict
from statistics import median

fruits=["apple", "banana", "apricot", "blueberry", "avocado", "cherry"]
res=defaultdict(list)

for f in fruits:
    res[f[0]].append(f)
print(res)

# Given two lists of integers, return a sorted list of all unique elements that appear in both lists (intersection) without using set operations directly on the lists.
# Sample Input: [1, 3, 5, 7, 9, 3] and [3, 4, 5, 6, 7, 5]
# Sample Output: [3, 5, 7]
A=[1, 3, 5, 7, 9, 3]
B=[3, 4, 5, 6, 7, 5]
list_a_unique=[]
list_dups=[]
for a in A:
    for b in B:
        if a==b:
            list_dups.append(a)
        else:
            list_a_unique.append(a)
print(list_dups)
list_unique=[]
for l in list_dups:
    if l not in list_unique:
        list_unique.append(l)
print(list_unique)

# Write a function that receives a list of tuples (name, age, city) and returns a nested dictionary
# grouped first by city, then by age range ("young" if age < 30, "adult" otherwise), containing lists of names.
# Sample Input: [("Alice", 25, "NY"), ("Bob", 35, "NY"), ("Charlie", 22, "LA"), ("Diana", 40, "LA")]
# Sample Output: {"NY": {"young": ["Alice"], "adult": ["Bob"]}, "LA": {"young": ["Charlie"], "adult"

import pandas as pd
inp =[("Alice", 25, "NY"), ("Bob", 35, "NY"), ("Charlie", 22, "LA"), ("Diana", 40, "LA")]

my_d=defaultdict(list)
for i in inp:
    my_d[i[2]].append([i[0],i[1]])
print(my_d)
results=defaultdict(lambda: defaultdict(list))
for k,v in my_d.items():
    for i,j in v:
        if j>30:
            results[k]['adult'].append(j)
        else:
            results[k]['young'].append(j)
print(results)

# Given a string of space-separated words, return the k most frequent words as a
# list of tuples (word, count), sorted by frequency descending, then alphabetically ascending for ties.
# Sample Input: text = "the day is the day is sunny sunny sunny is the", k = 2
# Sample Output: [("the", 3), ("is", 3)]

text = "the day is the day is sunny sunny sunny is the"
text_to_list=text.split()
print(text_to_list)
word_count=defaultdict(int)
for w in text_to_list:
    word_count[w]+=1
s_text=sorted(word_count.items(),reverse=True)
print(s_text)


# Given a dictionary of item prices and a list of purchased items
# (with possible duplicates), return the total cost after applying a discount rule: every third identical item is free.
# Sample Input: prices = {"apple": 2, "banana": 1, "orange": 3}, cart = ["apple", "apple", "apple", "banana", "orange", "orange"]
# Sample Output: 11


prices = {"apple": 2, "banana": 1, "orange": 3}
cart = ["apple", "apple", "apple", "banana", "orange", "orange"]
cart_num=defaultdict(int)
for c in cart:
    cart_num[c]+=1
print(cart_num)
rs=defaultdict(list)
for k,v in prices.items():
    for x,y in cart_num.items():
        if k==x:
            if y%3==0:
                x1=y//3
                rs[k].append(v*(y-x1))
            else:
                rs[k].append(v * y)
total=sum((list(rs.values())),[])
print(sum(total))
#
# Given a list of strings, group them into anagrams and return a list of groups,
# where each group is sorted alphabetically, and the groups themselves are sorted by the first word of each group.
# Sample Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]

word=["eat", "tea", "tan", "ate", "nat", "bat"]
words=defaultdict(list)
for w in word:
    key=''.join(sorted(w))
    words[key].append(w)
print(words)

#
# Implement a function that takes two sorted lists and returns a new
# sorted list containing the median of every pair of corresponding elements after merging the two lists into one sorted sequence (handle odd/even lengths properly).
# Sample Input: [1, 3, 5] and [2, 4, 6]
# Sample Output: [1.5, 2.5, 3.5, 4.5, 5.5]
a = [1, 3, 5]
b = [2, 4, 6]

merged = sorted(a + b)

result = []

for i in range(len(merged) - 1):
    median = (merged[i] + merged[i + 1]) / 2
    result.append(median)

print(result)
#
# Given a list of integers and a target sum, return all unique pairs of indices (i, j)
# such that i < j and the sum of the elements at those indices equals the target.
# Indices must be returned in ascending order of i, then j.
# Sample Input: nums = [2, 7, 11, 15, 7], target = 9
# Sample Output: [(0, 1), (0, 4)]

nums = [2, 7, 11, 15, 7]
target = 9

result = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            result.append((i, j))

print(result)
