"""Lists

Longest Consecutive Subsequence
Given a list of integers:
nums = [100, 4, 200, 1, 3, 2, 5]
Find the length of the longest consecutive subsequence (not necessarily contiguous in the list).
Pair with Given Sum (Return Indices)
Given a list nums = [2, 7, 11, 15, 3, 6] and a target target = 9,
return all unique pairs of indices (i, j) where nums[i] + nums[j] == target and i < j. Return as a list of tuples."""

nums = [100, 4, 200, 1, 3, 2, 5]
newnums= sorted(nums)
print(newnums)
nums = [100, 4, 200, 1, 3, 2, 5]
nums.sort()

result = []
temp = [nums[0]]

for i in range(1, len(nums)):
    if nums[i] == nums[i - 1] + 1:
        temp.append(nums[i])
    elif nums[i] == nums[i - 1]:
        continue  # ignore duplicates
    else:
        result.append(temp)
        temp = [nums[i]]

result.append(temp)

print(result)

nums = [2, 7, 11, 15, 3, 6]
t=9
val =[]
for i in range(len(nums)):
    for j in nums:
        if nums[i]+j==t and i<j:
            val.append(j)
print(dict(zip(nums,val)))
x=dict(zip(nums,val))
print(list(x.items()))

