"""

1. Given a 1D NumPy array of integers, create a dictionary where keys are the unique values and values are lists of their indices.

2. Create a 6x6 random integer array (values 0-20). Use a dictionary to map values: if value < 8 → 'low', 8-14 → 'medium', >14 → 'high'. Return a new array with these string labels.

3. Convert each row of a 4x5 NumPy array into a dictionary (keys as column indices or custom names). Collect all row dictionaries into a list.

4. Given two 1D NumPy arrays A and B of same length, create a dictionary where keys are tuples (A[i], B[i]) and values are the count of occurrences of that pair.

5. Implement a function that takes a 2D NumPy array and returns a dictionary of dictionaries representing a sparse matrix (only store non-zero elements with (row,col) as tuple keys).

6. For a 1D array of length n, create a dictionary where each key is the starting index of a rolling window of size 4, and the value is the subarray (as NumPy array) for that window.

7. Given a 2D NumPy array, sort the rows based on a custom ordering defined by a dictionary that assigns weights to each possible value. Return the sorted array.

8. Create a dictionary from a 3D NumPy array where keys are (layer, row) tuples and values are the mean of that row slice.

9. Merge two 2D arrays (same number of rows) by creating a list of dictionaries, where each dict combines corresponding rows from both arrays with prefixed keys like 'a_' and 'b_'.

10. Given a 1D NumPy array, build a binary tree-like nested dictionary structure where each level splits the array into left/right halves recursively (store min/max/sum at each node).

11. Use a default dictionary of lists to group elements from a 2D NumPy array by their column-wise sum. Return the grouped dictionary.

12. Create a 5x5 matrix of random floats. Replace values based on a lookup dictionary that maps value ranges to specific replacement numbers. Use vectorized operations where possible.

13. Convert a list of dictionaries (each containing numeric values) into a single 2D NumPy array, then compute column-wise statistics and store results back into a new dictionary.

14. Given a NumPy array and a separate list of labels, create a dictionary where keys are unique labels and values are the sub-arrays (slices) corresponding to each label group.

15. Implement an intermediate-level task: flatten a nested dictionary containing NumPy arrays at the leaves, then reconstruct a new nested structure after performing element-wise operations on all arrays.
"""

# Given a 1D NumPy array of integers, create a dictionary where keys are the unique values and values are lists of their indices.


import numpy as np
from collections import defaultdict

from Basic.L46 import count

my_array=np.random.default_rng().integers(0,100,10)
print(my_array)
lst=defaultdict(int)
freq = {val: np.sum(my_array == val) for val in np.unique(my_array)}
print(freq)

# Create a 6x6 random integer array (values 0-20). Use a dictionary to map values: if value < 8 → 'low', 8-14 → 'medium', >14 → 'high'. Return a new array with these string labels.

new_arr= np.random.default_rng().integers(0,20,(6,6))
print(new_arr)

my_dict={key:('low' if key<8 else 'high' if (key>8 & key<=14)  else key) for key in np.unique(new_arr)}
print(my_dict)

# 3. Convert each row of a 4x5 NumPy array into a dictionary (keys as column indices or custom names). Collect all row dictionaries into a list.

myarr=np.random.default_rng().integers(0,10,(4,5))
print('/n',myarr)
rows = [{f'col{i}': row[i] for i in range(myarr.shape[1])} for row in myarr]
print(rows)

# 4. Given two 1D NumPy arrays A and B of same length, create a dictionary where keys are tuples (A[i], B[i]) and values are the count of occurrences of that pair.
from collections import Counter
arr1=np.random.default_rng().integers(0,10,(2,2))
arr2=np.random.default_rng().integers(10,20,(2,2))
print(arr1)
print(arr2)
val={(a,b) for a,b in zip(arr1.flat,arr2.flat)}
print(val)
val_rows = {tuple(row1) : tuple(row2) for row1, row2 in zip(arr1, arr2)}
print(val_rows)

val_elementwise = {(int(a), int(b)) for a, b in zip(arr1.flat, arr2.flat)}
print(val_elementwise)
# pair_counts = Counter(zip(arr1.tolist(), arr2.tolist()))   # .tolist() prevents unhashable issues
# print(pair_counts)
# Or without Counter (pure dict):
pair_counts={}
for a, b in zip(arr1.flat, arr2.flat):
    key = (int(a), int(b))          # ensure Python scalars
    pair_counts[key] = pair_counts.get(key, 0) + 1

print(pair_counts)

# 5. Implement a function that takes a 2D NumPy array and returns a dictionary of dictionaries representing a sparse matrix (only store non-zero elements with (row,col) as tuple keys).

def sparse_matrix(arr):
    if not isinstance(arr,np.ndarray) or arr.ndim!=2:
        raise ValueError("Input must be 2D array")
    sparse = {}
    for i in range(arr.shape[0]):
        row_dict = {}
        for j in range(arr.shape[1]):
            val = arr[i, j]
            if val != 0:
                row_dict[j] = val  # inner dict: col -> value
        if row_dict:  # only add non-empty rows
            sparse[i] = row_dict

    return sparse
