"""Lists

Rotate List by K Positions
Given a list nums = [1, 2, 3, 4, 5, 6, 7] and an integer k = 3, rotate the list to the right by k positions.
Expected output: [5, 6, 7, 1, 2, 3, 4]
(Solve it in O(n) time and O(1) extra space if possible)
Find All Anagrams in a List
Given a list of words:
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Group the words that are anagrams of each other and return them as a list of lists."""
from collections import defaultdict
nums = [1, 2, 3, 4, 5, 6, 7]
k=3

k =k % len(nums)
result = nums[-k:]+ nums[:-k]
print(result)

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = defaultdict(list)

[groups[''.join(sorted(word))].append(word) for word in words]
print(groups)
print(list(groups.values()))