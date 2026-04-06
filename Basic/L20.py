from random import randint
L = []
for i in range(20):
    L.append(randint(1,100))
print("the list is ", L)
print("avg of items", (sum(L)/len(L)))
print("max of items", max(L))
print("min of items", min(L))
L.sort()
print("the sorted list is ", L)
print("second largest", L[-2])
print("second smallest", L[1])
even =0
for i in range(len(L)):
    if L[i] % 2 == 0:
        even += 1
print("no of even number", even)