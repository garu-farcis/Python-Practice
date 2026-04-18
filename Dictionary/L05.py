"""Create a 5 ×5 list of numbers. Then write a program that creates a dictionary whose keys are
the numbers and whose values are the how many times the number occurs. Then print the
three most common numbers."""
from collections import defaultdict

L=[[i for i in range(5)] for j in range(5)]
print(L)
x=[]
# d = defaultdict(list)
# for k in L:
#     for v in k:
#         x.append([v][v.count()])
# print(d)
flat =[j for m in L for j in m]
my_dict ={ flat[i]:flat.count(i) for i in  set((flat)) }
print(my_dict)