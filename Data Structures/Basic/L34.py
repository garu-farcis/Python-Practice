"""Write a program that creates and prints an 8 ×8 list whose entries alternate between 1 and 2
in a checkerboard pattern, starting with 1 in the upper left corner"""

L = [[1 if (i+j)%2==0 else 2 for i in range(8)] for j in range(8) ]
print(L)