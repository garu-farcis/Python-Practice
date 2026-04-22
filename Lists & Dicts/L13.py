"""Lists
Merge Overlapping Intervals
Given a list of intervals:
intervals = [[1,3],[2,6],[8,10],[15,18]]
Merge all overlapping intervals and return the result.
Expected output: [[1,6],[8,10],[15,18]]
Product of Array Except Self
Given:
nums = [1, 2, 3, 4]
Return a list where each element is the product of all other elements except itself.
Expected output: [24, 12, 8, 6]
(Do NOT use division; aim for O(n) time)"""

interval = [[1,3],[2,6],[8,10],[15,18]]


def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for i in intervals:
        # If merged list is empty OR no overlap
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            # Overlapping → merge
            merged[-1][1] = max(merged[-1][1], i[1])

    return merged
print(merge_intervals(interval))

nums = [1, 2, 3, 4]
results=[]
for i in range(len(nums)):
    prod=1
    for j in range(len(nums)):
        if i!=j:
            prod*=nums[j]
    results.append(prod)
print(results)
