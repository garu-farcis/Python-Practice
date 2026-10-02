"""1. Given an array of integers nums and an integer k, return the maximum sum of any contiguous subarray of size exactly k
 after performing at most one replacement of any element with any other integer.
Sample Input: nums = [1, -2, 3, 4, -5], k = 3
Sample Output: 10   (replace -5 with 6 → [1, -2, 3, 4, 6] → subarray [3,4,6])"""

nums = [1, -2, 3, 4, -5]
k = 3
nums[-1]=6
sub_array=[]
for num in range(len(nums)+1):
    sub_array.append((nums[num:num+k]))
print(sub_array)
sum_array={i:sum(sub_array[i]) for i in range(len(sub_array))}
print(sum_array)
my_key=[]
for k,v in sum_array.items():
    if v==max(sum_array.values()):
        my_key.append(k)
    else:
        pass
print(my_key)
print(f"the maximum sum of any contiguous subarray of size exactly k after performing at most one replacement of any element with any other integer {sub_array[my_key[0]]} ")

