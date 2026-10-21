"""Write a function that receives a list of integers and
returns the length of the longest consecutive sequence of numbers (numbers do not need to be adjacent in the list).
Sample Input: [100, 4, 200, 1, 3, 2, 5]
Sample Output: 5"""
from mypy.checkexpr import defaultdict

num = [100, 4, 200, 1, 3, 2, 5]
my_set=set(num)
longest=0
for n in my_set:
    if n-1 not in my_set:
        current=n
        length=1

        while current+1 in my_set:
            current+=1
            length+=1

    longest=max(longest,length)
print(longest)


# Given a list of strings, group them into anagrams and return a list of groups,
# where each group is sorted alphabetically, and the groups themselves are sorted by the first word of each group.
# Sample Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
from collections import defaultdict

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = defaultdict(list)

for word in words:
    key = ''.join(sorted(word))
    groups[key].append(word)

result = []

for group in groups.values():
    group.sort()
    result.append(group)

result.sort(key=lambda x: x[0])

print(result)


