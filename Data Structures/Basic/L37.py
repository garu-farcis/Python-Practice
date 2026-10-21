"""Write a program that creates a 10 ×10 list of random integers between 1 and 100. Then do the
following:
(a) Print the list.
(b) Find the largest value in the third row.
(c) Find the smallest value in the sixth column."""
from random import randint
from pprint import pprint
L =[[(randint(1,100)) for i in range(10)] for j in range(10)]
pprint(L)
row =2
val = [L[row][i] for i in range(len(L))]
pprint(val)
print("max of 3rd row is ", max(val))
col = 5
val1 = [L[i][col] for i in range(len(L))]
pprint(val1)
print("min of 6th col is ", min(val1))