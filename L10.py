x =int(input("enter row number"))
y = int(input("enter column number"))
matrix=[]
for i in range(x):
    num =[' '] * y
    matrix.append(num)
matrix1=[]
for i in range(x):
    num =[' '] * y
    matrix1.append(num)
num = 0
for i in range(x):
    for j in range(y):
        matrix[i][j] = str(num)
        num = (num + 1) % 10

for n in matrix:
    print(' '.join(n))