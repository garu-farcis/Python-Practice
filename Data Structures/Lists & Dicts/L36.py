"""Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters. You must solve it in O(n) time.
Sample Input: s = "eceba", k = 2
Sample Output: 3   ("ece")"""

s = "eceba"
k = 2
myls=list(s)
print(myls)
print(len(s))
als=[]
for i in range(len(myls)-k+1):
    als.append(myls[i:i+k])
max_el=[]


print(max_el)
# . Given a string s containing only lowercase letters,
# return the minimum number of characters that need to be deleted so that the frequency of every remaining character is unique.
# Sample Input: s = "aabbcc"
# Sample Output: 3   (delete one a, one b, one c → frequencies become 1,1,1 which are not unique; better delete all of one letter)
s = "aabbcc"
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print(freq)
used = set()
deletions = 0
for count in freq.values():
    while count > 0 and count in used:
        count -= 1
        deletions += 1
    if count > 0:
        used.add(count)
print(deletions)

#
# . Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.
# You must solve it in O(n) time and O(1) extra space (excluding the output array).
# Sample Input: nums = [-7, -3, 2, 3, 11]
# Sample Output: [4, 9, 9, 49, 121]

nums = [-7, -3, 2, 3, 11]
# sor_num=sorted(nums,reverse=True)
# print(sor_num)
# This is non-decreasing because each number is either:
#
# greater than the previous number, or
# equal to the previous number.

sor_num=[]
for i in range(len(nums)-1):
    if nums[i+1]>=nums[i]:
        sor_num.append(nums[i]*nums[i])
print(sor_num)