"""DSA
1. max value"""

L=[10,89,74,276,847,74,273,773,93,1004,74747]
my_len=len(L)
print(my_len)
max0=0
for i in range(0,my_len-1):
    if L[i]>L[i+1]:
        max=L[i]
        L[i]=L[i+1]
        L[i+1]=max
print(L[-1])

"""Bubble Sorting Algorithm"""

L=[10,89,74,276,847,74,273,773,93,1004,74747]
my_len=len(L)
for i in range(0,my_len-1):
    for j in range(0,my_len-i-1):
        if L[j]>L[j+1]:
            max0=L[j]
            L[j]=L[j+1]
            L[j+1]=max0
print(L)

"""Minimum value"""
L=[89,12,9,74,276,847,74,273,773,93,1004,74747]
my_len=len(L)
min_index=0
for i in range(0,my_len):
    if L[min_index]>L[i]:
        min_index=i
        print(L[min_index])

"""Select Sorting Algorithm"""

L=[89,12,9,74,276,847,74,273,773,93,1004,74747]
my_len=len(L)
min_index=0
# temp=0
for i in range(0,my_len):
    min_index=i
    # min_val=L[min_index]
    for j in range(i+1,my_len):
        if L[j]<L[min_index]:
            min_index = j

    if min_index!=i:
        # temp=L[i]
        L[i],L[min_index]=L[min_index],L[i]
print(L)


"""Insert Sorting Algorithm"""
L=[89,12,9,74,276,847,74,273,773,93,1004,74747]
my_len=len(L)
# keys=70
# keys=0
for i in range(0,my_len):
    keys=L[i]
    j=i-1
    while j>=0 and L[j]>keys:
        L[j+1]=L[j]
        j-=1
    L[j+1]=keys
print(L)

"""Reverse Array"""
L=[89,12,9,74,276,847,74,273,773,93,1004,74747]
print(L[::-1])
for i in range(0,len(L)//2):
    L[i],L[my_len-i-1]=L[my_len-i-1],L[i]
print(L)


"""Dichotomy Binary Search"""

#  linear search
L=[89,12,9,74,276,847,74,273,773,93,1004,74747]
my_ind=74
val= [i for i in range(len(L)) if L[i]==my_ind]
print(val)

# binary search can be performed only on sorted arrays
L=[89,12,9,74,276,847,74,273,773,93,1004,74747]
L.sort()
print(f'sorted {L}'.format(L))
low=0
high=len(L)-1
# mid=(low+high)//2
# print(mid)
search_val=74
found=False
while low<=high:
    mid = (low + high) // 2
    if L[mid]==search_val:
        print("Found at index:", mid)
        found = True
        break
    elif L[mid]<search_val:
        low=mid+1
    else:
        high =mid-1
if not found:
    print('not found')

"""Shell Sorting"""
