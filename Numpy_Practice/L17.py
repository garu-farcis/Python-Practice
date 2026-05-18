""". Group-wise Aggregation Without Pandas
Problem

Given:

values = np.array([10,20,30,5,15])
groups = np.array([1,1,1,2,2])

Compute:

sum per group
mean per group
count per group
Expected Output
{
 1: {'sum':60, 'mean':20, 'count':3},
 2: {'sum':20, 'mean':10, 'count':2}
}"""

import numpy as np
values = np.array([10,20,30,5,15])
groups = np.array([1,1,1,2,2])
my_groups=np.unique(groups)
my_dict={}
for g in my_groups:
    vals=values[groups==g]
    my_dict[g]={
        'sum': vals.sum(),
        'mean': vals.mean(),
        'count': len(vals)
    }
print(my_dict)

"""Rolling Window Statistics
Problem

Given a time series:

arr = np.arange(1,11)

Compute:

3-day rolling mean
output same length
first 2 positions should be NaN
Expected Output
[nan, nan, 2., 3., 4., 5., 6., 7., 8., 9.]
Tests
np.convolve
padding
window operations"""
arr = np.arange(1,11)
import numpy as np

arr = np.arange(1, 11)

window = 3

rolling_mean = np.convolve(
    arr,
    np.ones(window) / window,
    mode='valid'
)

result = np.concatenate([
    np.full(window - 1, np.nan),
    rolling_mean
])

print(result)
# print(result[:,:,1])