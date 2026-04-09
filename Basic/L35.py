"""Write a program that checks to see if a 4 ×4 list is a magic square. In a magic square, every
row, column, and the two diagonals add up to the same value."""

L = [ [j for i in range(4)] for j in range(4)]
print(L)
sum_of_rows=[]

for i in range(4):
    sums = 0
    for j in range(4):
        sums = sums+L[i][j]
    sum_of_rows.append(sums)
print(sum_of_rows)
sum_of_columns=[]
for i in range(4):
    sums = 0
    for j in range(4):
        sums = sums+L[j][i]
    sum_of_columns.append(sums)
print(sum_of_columns)
target_sum = sum(L[0])
if sum(L[i][i] for i in range(4)) != target_sum:
    magic = False
    print(magic)
if sum(L[i][3-i] for i in range(4)) != target_sum:
    magic = False
    print(magic)
print("Magic Square" if magic else "Not a Magic Square")