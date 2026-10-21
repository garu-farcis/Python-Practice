"""The following is useful as part of a program to play Minesweeper. Suppose you have a 5 ×5
list that consists of zeros and M’s. Write a program that creates a new 5 ×5 list that has M’s in
the same place, but the zeroes are replaced by counts of how many M’s are in adjacent cells
(adjacent either horizontally, vertically, or diagonally). An example is shown below. [Hint:
short-circuiting may be helpful for avoiding index-out-of-range errors.]
0 M 0 M 0
0 0 M 0 0
0 0 0 0 0
M M 0 0 0
0 0 0 M 0


1 M 3 M 1
1 2 M 2 1
2 3 2 1 0
M M 2 1 1
2 2 2 M 1"""
from pprint import pprint
L = [[0, 'M', 0, 'M', 0],
    [0, 0 ,'M', 0, 0],
    [0 ,0 ,0 ,0, 0],
    ['M','M', 0, 0, 0],
    [0 ,0 ,0 ,'M' ,0]
    ]
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),(0, 1),
    (1, -1),  (1, 0), (1, 1)
]
rows = len(L)
cols = len(L[0])
val = 'M'
for i in range(rows):
    for j in range(cols):
        if L[i][j] == val:
            continue
        else:
            counter =0
            for r, c in directions:
                side_row = i + r
                side_col = j + c

                if 0 <= side_row < rows and 0 <= side_col < cols:
                    if L[side_row][side_col] == 'M':
                        counter += 1

        L[i][j] = str(counter)
pprint(L)