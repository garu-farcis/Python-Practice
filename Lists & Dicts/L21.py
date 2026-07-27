"""1. Write a function that takes a list of integers and returns a new list with only the even numbers, squared."""
def squared(numlst):
    print(f"your list is{numlst}")
    evenlst=[i for i in numlst if i%2==0]
    print(f"your even number list if {evenlst}")
    powlst=[i*i for i in numlst if i%2==0]
    return powlst

mylst=[2,4,3,554,64,22,1,2,122,322,43,54]
val=squared(mylst)
print(f"your even squared list is {val}")

"""2. Write a function that counts the frequency of each character in a string (ignore case and spaces)."""

from collections import defaultdict
def counter(mystr):
    print(f"my string is {mystr}")
    mystrlist=[each for each in mystr]
    print(f"the string as a list {mystrlist}")
    freq=defaultdict(int)
    # mydict={each:each.count() for each in mystrlist}
    for each in mystrlist:
        freq[each]+=1
    return freq

# mystring= str(input("enter a string"))
mystring="helloeveryonehow islife"
print(mystring)
myval=counter(mystring)
print(f"the dictonary of freq with char is {myval}")

"""3. Implement a function that flattens a nested list of arbitrary depth."""

def flattens(mylst):
    print(f"your list is{mylst}")
    res=[]
    for each in mylst:
        if isinstance(each,list):
            res.extend(flattens(each))
        else:
            res.append(each)
    return res

lst=[3,54,[2,[4,5,[33,54,66]],44,67,43]]
res=flattens(lst)
print(f"flattened list is {res}")