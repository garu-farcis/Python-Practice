"""We usually refer to the entries of a two-dimensional list by their row and column, like below
on the left. Another way is shown below on the right.
(0,0) (0,1) (0,2) 0 1 2
(1,0) (1,1) (1,2) 3 4 5
(2,0) (2,1) (2,2) 6 7 8
(a) Write some code that translates from the left representation to the right one. The //and
%operators will be useful. Be sure your code works for arrays of any size.
row = index // number_of_columns
col = index % number_of_columns
index = row * number_of_columns + column
(b) Write some code that translates from the right representation to the left one."""

L = [[(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)]]
print(L)
Lnew= [j for m in L for j in m]
print(Lnew)
cols = 3
indices = [row * cols + col for (row, col) in Lnew]
print(indices)