"""Given a string of space-separated words, return the k most frequent words
 as a list of tuples (word, count), sorted by frequency descending, then alphabetically ascending for ties.
Sample Input: text = "the day is the day is sunny sunny sunny is the", k = 2
Sample Output: [("the", 3), ("is", 3)]"""
from collections import defaultdict
strng="the day is the day is sunny sunny sunny is the"
my_str=strng.split(' ')
print(my_str)
word_count=defaultdict(int)
for word in my_str:
    word_count[word]+=1
print(word_count)
res=defaultdict(list)
print(sorted(word_count.items(),reverse=True,key=lambda x: x[1]))
