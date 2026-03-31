x =4
y =4
# matrix=[4][4]  cmd + /
matrix =[]
for i in range(x):
    num =[' '] * y
    matrix.append(num)
for i in range(x):
    for j in range(y):
        if i==0 or i==x-1 or j==0 or j==y-1:
            matrix[i][j]='*'

for x in matrix:
    print(' '.join(x))
