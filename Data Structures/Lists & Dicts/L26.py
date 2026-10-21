"""3. Implement a function that takes a list of strings and returns a
dictionary where keys are the unique first characters and values are sorted lists of all words starting with that character.
Sample Input: ["apple", "banana", "apricot", "blueberry", "avocado", "cherry"]
Sample Output: {"a": ["apple", "apricot", "avocado"], "b": ["banana", "blueberry"], "c": ["cherry"]}"""

from collections import defaultdict
lst=["apple", "banana", "apricot", "blueberry", "avocado", "cherry"]
my_dict=defaultdict(list)
for val in lst:
    my_dict[val[0]].append(val)
print(my_dict)