"""Remove Duplicates While Preserving Order
Given a list that may contain duplicates, write a function that returns a new list with duplicates removed while maintaining the original order of first occurrence.
PythonInput: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
Output: [3, 1, 4, 5, 9, 2, 6]"""
from itertools import groupby

import numpy as np
L= [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
res= np.array(list(dict.fromkeys(L)))
print(res)


"""Group and Aggregate Orders
Given a list of dictionaries representing orders, group them by customer_id and calculate the total amount spent by each customer. Return a dictionary with customer_id as key and total amount as value.
Python orders = [
    {"customer_id": 101, "amount": 250.5},
    {"customer_id": 102, "amount": 150.0},
    {"customer_id": 101, "amount": 300.75},
    ...
]"""


orders = [
    {"customer_id": 101, "amount": 250.5},
    {"customer_id": 102, "amount": 150.0},
    {"customer_id": 101, "amount": 300.75},
    {"customer_id": 103, "amount": 300.75}
]

from collections import defaultdict, Counter

d=defaultdict(int)
for order in orders:
    d[order["customer_id"]] += order["amount"]
print(d)

"""Find Common Elements Efficiently
Given two lists a and b (each up to 1 million elements), return the intersection (common elements) as a list. Optimize for both time and space. 
Provide at least two different approaches and discuss trade-offs."""


a=np.arange(1000)
b=np.arange(10000)

res=np.intersect1d(a,b)
print(res)
res1=list(set(a) & set(b))
print(res1)


"""Frequency Count with Threshold
Write a function that takes a list of strings (e.g., event types) and 
returns a dictionary of items that appear more than k times. Use the most Pythonic and efficient way."""

from collections import Counter
def str_meth(my_string,val):
    lists_of_lists=defaultdict(list)
    for each in my_string:
        for i in each:
            lists_of_lists[each].append(i)
    print(lists_of_lists)

    # for key,group in groupby(lists_of_lists.values(),key=lambda x:x):
    #     freq[key].append(list(group))
    # print(freq)
    # for val in lists_of_lists.values():
    #     freq1={}
    #     for e in val:
    #         freq1[e]=freq1(e,0)+1
    # # print(freq)
    # for e in my_string:
    #         freq=Counter(my_string)
    #         print(freq)
    # my_list={key:val for key,val in freq.items() if val> k}
    # print(my_list)
    result = []

    for word in my_string :
        freq = Counter(word)  # count chars
        print(freq)
        max_freq = max(freq.values())  # highest frequency
        print(max_freq)
        result.append((word, max_freq))

    # sort by frequency descending
    result.sort(key=lambda x: x[1], reverse=True)
    return result




my_str=['hi','hf','hdgjwdg','jhgjg','nsvdgh']
k=2
str_meth(my_str,k)


"""Tuple-Based Configuration
You are given a list of tuples representing (user_id, session_id, duration). 
Write a function to find the user with the maximum total session duration. Return (user_id, total_duration).
Why might using tuples here be better than lists?"""
import builtins
sessions = [
    (101, 's1', 35.5),
    (102, 's2', 20.0),
    (101, 's3', 15.25),
    (103, 's4', 50.0),
    (102, 's5', 45.75),
    (101, 's6', 10.0),
    (104, 's7', 60.5),
    (103, 's8', 25.0)
]
def tuple_total(session):
    res=defaultdict(list)
    sum_all=defaultdict(int)
    session = sorted(session, key=lambda x: x[0])
    for key,group in groupby(session,key=lambda x:x[0]):
        # res[key].append(list(group))
        total=sum((i[2]) for i in group)
        sum_all[key] = total
    max_user = max(sum_all, key=sum_all.get)
    print(sum_all)
    # print(res)
    print(max_user)
    return max_user, sum_all[max_user]

tuple_total(sessions)


"""Dictionary Merge with Conflict Resolution
Given two dictionaries dict1 and dict2, merge them such that if a key exists in both, 
keep the value from dict2 but also store the old value from dict1 under a new key like old_{key}. Handle nested dicts is a bonus."""


dict1 = {
    "name": "Alice",
    "age": 25,
    "city": "Paris"
}

dict2 = {
    "name": "Bob",
    "salary": 50000,
    "department": "HR"
}
merged={}
d=defaultdict(list)
for k,v in dict1.items():
    if k in dict2.keys():
        # merged[f"old_{k}"] = merged[k]
        # merged[k] = v
        d[k].append(dict2[k])
        d['old_'+k].append(v)
print(d,merged)


"""Anagram Grouping
Given a list of strings, group the anagrams together and return a list of lists 
(each inner list contains anagrams). Use appropriate data structures."""

words = [
    # Anagram groups:
    "listen",
    "silent",
    "enlist",
    "tinsel",

    "triangle",
    "integral",
    "alerting",

    "debit card",
    "bad credit",

    "dormitory",
    "dirty room",

    # Non-anagrams (don't belong to any group above):
    "hello",
    "world",
    "python",
    "programming",
    "apple",
    "banana",
    "computer",
    "keyboard"
]
groups=defaultdict(list)
words=[i.strip() for i in words]
for word in words:
    my_count=Counter(word)
    print(my_count)
    key = ''.join(sorted(word))
    groups[key].append(word)
print(groups)





