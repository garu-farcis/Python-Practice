"""The following is useful in implementing computer players in a number of different games.
Write a program that creates a 5 ×5 list consisting of zeroes and ones. Your program should
then pick a random location in the list that contains a zero and change it to a one. If all the
entries are one, the program should say so. [Hint: one way to do this is to create a new list
whose items are the coordinates of all the ones in the list and use the choice method to
randomly select one. Use a two-element list to represent a set of coordinates.]"""

from random import choice
L =[[(0 if i%2 ==0 else 1) for i in range(5)] for j in range(5)]
print(L)
my_choice=[]
for i in range(len(L)):
    for j in range(len(L[i])):
         if L[i][j]==0:
            my_choice.append((i,j))
print(my_choice)
i,j = choice(my_choice)
print(i,j)
L[i][j]=1
print(L)

