"""1. Data Cleaning - Remove Invalid Rows
Given a 2D NumPy array of sensor readings, remove all rows that contain any NaN values.
Python
import numpy as np
data = np.array([
    [1.0, 2.0, 3.0],
    [4.0, np.nan, 6.0],
    [7.0, 8.0, 9.0],
    [np.nan, 11.0, 12.0]
])
Expected Output: Array with 2 rows: [[1,2,3], [7,8,9]]"""
from itertools import groupby

import numpy as np

from Dictionary.L06 import my_dict

data = np.array([
    [1.0, 2.0, 3.0],
    [4.0, np.nan, 6.0],
    [7.0, 8.0, 9.0],
    [np.nan, 11.0, 12.0]
])

print(data[~np.any(np.isnan(data),axis=1)])

"""2. Column-wise Normalization (Z-score)
Normalize each column of a 2D array so that every column has mean = 0 and standard deviation = 1.
Input: Shape (1000, 5) random float array
Output: Same shape, each column standardized"""
my_arr=np.random.rand(1000,5)
print(my_arr)
mean = np.mean(my_arr, axis=0)
std = np.std(my_arr, axis=0)
normalized = (my_arr - mean) / std
print(normalized)

"""3. Filter Transactions Above Threshold
Given a 1D array of transaction amounts, return all amounts greater than the 90th percentile.
Python
amounts = np.random.normal(500, 100, 10000)
Return the filtered array sorted in descending order."""

amounts = np.random.normal(500, 100, 10000)
# print(np.all(amounts[np.percentile(amounts,90)],)
print(amounts[amounts>np.percentile(amounts,90)])
x=amounts[amounts>np.percentile(amounts,90)]
filtered_sorted = np.sort(x)[::-1]
print(filtered_sorted)

"""4. Group Mean by Category
You have two arrays:

values: shape (n,) → numeric values
labels: shape (n,) → category labels (strings)

Compute the mean value for each unique label.
Sample:
Python
values = np.array([10, 15, 20, 25, 30])
labels = np.array(['A', 'B', 'A', 'B', 'A'])
Expected: {'A': 20.0, 'B': 20.0} (return as dict)"""
values = np.array([10, 15, 20, 25, 30])
labels = np.array(['A', 'B', 'A', 'B', 'A'])
v=list(values)
l=list(labels)
from collections import defaultdict
d=defaultdict(list)
for k,v in zip(labels,values):
    d[k].append(v)
print(d)
print({k:np.mean(v) for k,v in d.items()})

"""5. Rolling Average (Moving Average)
Compute 7-day rolling mean for a time series array. Use only NumPy (no pandas).
Input: 1D array of length 30
Output: 1D array of length 30 (use NaN for first 6 positions)"""
lst=np.arange(30)
window=7
kernel = np.ones(window) / window
roll = np.convolve(lst, kernel, mode='valid')
result = np.full(lst.shape, np.nan)
result[window-1:] = roll

"""6. Top N Records per Column
Given a 2D array of shape (10000, 8), find the top 5 highest values and their row indices for each column.
Return a dictionary with column index as key.

7. Vectorized Euclidean Distance
Given two 2D arrays A and B both of shape (n, d), compute Euclidean distance between corresponding rows (row-wise).
Input shape: (5000, 10) for both
Output: 1D array of shape (5000,)"""

my_lst= np.random.default_rng().integers(0,1000,size=(10000,8))
sorted_indx=np.argsort(my_lst,axis=0)
d1={}
top_5=sorted_indx[-5:,:]
# # print(top_5)
# my_keys=[my_lst[i] for i in top_5]
# print(my_keys)
# #
# # print(top_5keys)
# for k,v in zip(my_keys,top_5):
#     d[k].append(v)
# print(d)
for col in range(my_lst.shape[1]):
    rows = top_5[:, col]
    values = my_lst[rows, col]

    d1[col] = (values, rows)
print(d1)

"""8. Replace Outliers
Given a 1D array, replace all values below 5th percentile and above 95th percentile with the median value.
Do it in a vectorized manner."""
my_lst= np.random.default_rng().integers(0,1000,size=5)
below_5=np.percentile(my_lst,5)
above_95=np.percentile(my_lst,95)
median = np.median(my_lst)
result = np.where(
    (my_lst < below_5) | (my_lst > above_95),
    median,
    my_lst
)
print(result)

"""9. Array Conversion from List of Lists with Different Lengths
You receive data as a Python list of lists (some rows shorter). Convert it into a NumPy 2D array by padding shorter rows with NaN.
Sample Input:
Python
data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
Output: 2D array with shape (3, 4)"""

data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

rows=len(data)
col=max(len(i) for i in data)
my_arr= np.full((rows,col),np.nan)
print(my_arr.shape)

"""10. Boolean Mask Based on Multiple Conditions
Given a 2D array of shape (n, 4) representing [age, salary, score, dept_id], select rows where:

age > 25
salary > 50000
score >= 80
Return the filtered array.


11. Cumulative Sum by Group
Given values and group_id arrays, compute cumulative sum within each group.
Sample:
Python
values = np.array([10, 20, 30, 5, 15])
group_id = np.array([1, 1, 1, 2, 2])
Expected Output: [10, 30, 60, 5, 20]"""

my_arr = np.random.default_rng().integers(1, 100, size=(3,4))
keys = np.array(['age', 'salary', 'score', 'dept_id'])
col_idx = {name: i for i, name in enumerate(keys)}
salary_col = my_arr[:, col_idx['salary']]
print(salary_col > 50)

values = np.array([10, 20, 30, 5, 15])
group_id = np.array([1, 1, 1, 2, 2])
print(np.cumsum(values))
print(np.cumsum(group_id))


import numpy as np

values = np.array([10, 20, 30, 5, 15])
group_id = np.array([1, 1, 1, 2, 2])

# sort by group
order = np.argsort(group_id)

sorted_values = values[order]
sorted_groups = group_id[order]

# cumulative sum
cumsum = np.cumsum(sorted_values)

# reset at group changes
reset_points = np.r_[True, sorted_groups[1:] != sorted_groups[:-1]]

result_sorted = np.where(reset_points, sorted_values, cumsum - np.maximum.accumulate(np.where(reset_points, 0, cumsum)))

# restore original order
result = np.empty_like(result_sorted)
result[order] = result_sorted

print(result)