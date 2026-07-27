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

"""4. Write a function that finds the second largest unique number in a list. Return None if it doesn't exist."""

def secondlasrgest(mylst):
    print(f"the original list is {mylst}")
    res= sorted(mylst,reverse=True)
    print(f"Sorted list is {res}")
    if len(res)>1:
        print(f"second largest is {res[1]}")
    else:
        return None

mylst=[2,4,3,554,64,22,1,2,122,322,43,54]
results=secondlasrgest(mylst)


"""5. Create a class `BankAccount` with deposit, withdraw, and get_balance methods. Raise ValueError on insufficient funds."""

class Bankacc:
    def __init__(self,bal=0):
        self._bal=bal
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("ammount must be positive")
        self._bal +=amount
        print(f"the balance is {self._bal}")
    def withdraw(self,amount):
        if amount>self._bal:
            raise ValueError("amount cant be more than bal")
        self._bal -= amount
        print(f"the balance is {self._bal}")


    def get_balance(self):
        print(f"the balance is {self._bal}")
        return self._bal


acc=Bankacc(500)
acc.withdraw(200)
acc.deposit(300)
print(acc.get_balance())

"""6. Write a function that groups a list of words by their first letter into a dictionary."""
from itertools import groupby
def grouper(mystring):
    print(f"the original string is {mystring}")
    listoflist=[each for each in mystring]
    print(listoflist)
    groups=defaultdict(list)
    for each in listoflist:
        groups[each[0].lower()].append(each)
    return dict(groups)
myst=["jhgh",' djh',' sfg', 'jghdj',' hgfkfb','s skj',' wooe',' fdkj dfn'," wsfg svs"]
res=grouper(myst)
print(f"the result is {res}")



