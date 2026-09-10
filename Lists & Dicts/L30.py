"""You have a list of integers representing a circular array.
Return True if there exists a cycle of length greater than 1 where
consecutive elements point to the next index by their value (positive = forward, negative = backward).
Sample Input: [2, -1, 1, 2, 2]
Sample Output: True"""

lst= [2, -1, 1, 2, 2]
cir_lst=[]
for i in range(len(lst)):
    