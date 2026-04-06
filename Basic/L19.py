
L = []

L = list(input("Enter your list: "))
print("the list is ", L)

print("no of items", len(L))
counter =0
for i in range(len(L)):
    if '5' in L[i]:
        counter = counter + 1
if counter:
    print("yes 5 present")
else:
    print("no 5 present")
print("last item", L[-1])
print("reverse List", L[::-1])
print("no of fives", counter)
M=[]
for i in range(len(L[1:-2])):
    M.append(L[i])
M.sort()
print("new list" , M)