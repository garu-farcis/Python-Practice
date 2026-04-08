"""Use a list comprehension to produce a list that consists of all palindromic numbers between
100 and 1000"""
L = [i for i in range(100,1000)]
print(L)
L1= [i for i in L if str(i)==str(i)[::-1]]
print(L1)
print(len(L1))