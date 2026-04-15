"""Write a program that uses a boolean flag variable in determining whether two lists have any
items in common."""

mylist = input("enter your first list ")
L =[]
for i in mylist:
    L.append(i)
print(L)
mylsit1 = input("enter your second list ")
L1=[]
for i in mylsit1:
    L1.append(i)
print(L1)
flag =0
if L==L1:
    flag=1
else:
    flag=0
if flag:
    print("yes equal")
else:
    print("not equal")
    print(L+L1)
