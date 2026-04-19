"""Group anagrams: Given
words = ["eat", "tea", "tan", "ate", "nat", "bat"], return grouped lists: [["eat","tea","ate"], ["tan","nat"], ["bat"]].
Use a dictionary with sorted tuples as keys.
"""

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# L=[(k,[v]for v in words if words[v]==words[:]) for k,v in sorted(set(words),key=words.index)]
# l -words.sort()
# L ={k:[v for v in words if words[v]==words[:]] for k,v in set()}
# print(L)

groups = {}

for w in words:
    key = tuple(sorted(w))

    if key not in groups:
        groups[key] = []

    groups[key].append(w)

result = list(groups.values())

print(result)
