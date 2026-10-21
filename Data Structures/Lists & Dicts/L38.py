"""Write a function that takes a list of strings and groups the anagrams together.
Sample Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Sample Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]"""

from collections import defaultdict
lst=["eat", "tea", "tan", "ate", "nat", "bat"]
result=defaultdict(list)
for each in lst:
    key=''.join(sorted(each))
    result[key].append(each)
print(result.values())


# 4. Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid (brackets are closed in the correct order).
# Sample Input: "({[]})"
# Sample Output: True
# Sample Input: "([)]"
# Sample Output: False

my_str=['(', ')', '{', '}', '[',']']
sam_input='({[]})'
sam_input1='([)]'
in1=list(sam_input)
print(in1)
in2=list(sam_input1)
print(in2)
right1=-1
for left in range(len(my_str)):
    if my_str[left]!=right1:
        print("False")
        pass
    else:
        left=left+1




