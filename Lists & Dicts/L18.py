"""Find Leaders in an Array
Given a list:
nums = [16, 17, 4, 3, 5, 2]
An element is a “leader” if it is greater than all elements to its right.
Return all leaders in the list.
Expected output: [17, 5, 2]
Rearrange List Alternating High-Low
Given:
nums = [1, 2, 3, 4, 5, 6, 7]
Rearrange the list so that it becomes:
max, min, 2nd max, 2nd min, ...
Expected output: [7, 1, 6, 2, 5, 3, 4]"""
from collections import defaultdict
nums = [16, 17, 4, 3, 5, 2]
nums.reverse()
print(nums)
# res=[nums[n] for n in range(len(nums)) if nums[n]>nums[n+1]]
res=[]
max_right=0
for i in range(0,len(nums)):
    if nums[i]>max_right:
        res.append(nums[i])
        max_right=nums[i]

print(res[::-1])

nums = [1, 2, 3, 4, 5, 6, 7]
nums.sort()
print(nums)
result = []
for i in range(len(nums) // 2):
    result.append(nums[-(i+1)])
    result.append(nums[i])

if len(nums) % 2 != 0:
    result.append(nums[len(nums)//2])

print(result)
