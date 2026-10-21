"""Dictionaries

Word Frequency Counter with Length Filter
Given a sentence:
text = "Python is great and Python is powerful and Python is fun"
Create a dictionary that counts the frequency of each word, but only include words with length greater than 3.
Dictionary of Students and Their Subjects
Given a list of tuples: (student, subject)
enrollments = [('Alice', 'Math'), ('Bob', 'Physics'), ('Alice', 'Physics'), ('Charlie', 'Math'), ('Bob', 'Math'), ('Alice', 'Chemistry')]
Create a dictionary where each student maps to a set of subjects they are enrolled in.
Top K Frequent Words
Given a list of words:
words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date", "banana", "cherry"]
Return the top 2 most frequent words along with their counts as a list of tuples, sorted by frequency (highest first).
"""

from collections import defaultdict
text = "Python is great and Python is powerful and Python is fun"
print(text.split())
T= text.split()
groups =defaultdict(list)
freq={}
for each in T:
    if len(each)>5:
        freq[each]=freq.get(each,0)+1
print(freq)
# my_dict ={k :v for k,v in freq.items()}
# print(my_dict)

enrollments = [('Alice', 'Math'), ('Bob', 'Physics'), ('Alice', 'Physics'), ('Charlie', 'Math'), ('Bob', 'Math'), ('Alice', 'Chemistry')]
my_dict ={k:v for k,v in sorted(enrollments, key= lambda x:x[1])}
print(my_dict)
d=defaultdict(list)
for k,v in enrollments:
    d[k].append(v)
print(d)

words = ["apple", "banana", "apple", "cherry", "banana", "apple", "date", "banana", "cherry"]
freq={}
for each in words:
    freq[each]=freq.get(each,0)+1
print(freq)
max_values =max(freq.values())
print('max values',max_values)
L= [(k,v) for k,v in freq.items()]
print(L)
