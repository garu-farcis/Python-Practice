"""1. Write a function that takes a list of integers and returns a new list with only the even numbers, squared."""
from numpy.ma.extras import average


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

"""7. Implement a recursive function to compute the nth Fibonacci number efficiently using memoization."""
def fibo(limitaion):
    # print(f"the limit of your series is {limitaion}")
    if limitaion<2:
        return limitaion
    else:
        return fibo(limitaion-1)+fibo(limitaion-2)
lim=11
val=fibo(lim)
for i in range(0,lim+1):
    print(fibo(i), end=" ")
print(f"the value of fibo at position {lim} is {val}")

"""8. Write a function that removes all duplicates from a list while preserving the original order."""

def removedups(mylst):
    print(f"my list is {mylst}")
    unique=[]
    dups=[]
    for each in mylst:
        if each not in unique:
            unique.append(each)
        else:
            dups.append(each)
    print(f"duplicates are {dups}")
    # print(f"unique list is {unique}")
    return unique

lst=[3,4,5,65,6,4,4,4,3,2,2,5,46,6,7,65,44,3]
res=removedups(lst)
print(f"unique list with order preserved is {res}")


"""9. Create a function that takes a dictionary of student scores and returns the names of students who scored above the average."""

def students(scoresdct):
    print(f"score list is {scoresdct}")
    # scores=[v for v in scoresdct.values()]
    score_avg= sum(scoresdct.values()) / len(scoresdct)
    print(f"avg is {score_avg}")
    res_dct=defaultdict(list)
    for k,v in scoresdct.items():
        if v>=score_avg:
            res_dct[k].append(v)
        else:
            pass
    return res_dct.keys()

# score_lst=[10,24,54,44,46,22,28,34,40,44,54,55,32,24,22,42,23]
mydict={"Alice": 85, "Bob": 70, "Charlie": 95, "Diana": 60}
res=students(mydict)
print(f"the names of students who scored above the average {res} ")


"""10. Write a function that rotates a list to the right by k positions."""
def rotate_right(lst, k):
    if not lst:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_right([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]

"""11. Implement a simple stack class with push, pop, peek, and is_empty methods."""

class stackimplement:
    def __init__(self):
        self._items=[]
    def push(self,item):
        self._items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    def is_empty(self):
        return len(self._items)==0

s = stackimplement()
s.push(10)
s.push(20)
print(s.pop())   # 20
print(s.peek())

"""12. Write a function that finds all pairs of numbers in a list that sum to a target value. Return unique pairs."""

target_val=20
lst=[10,20,5,15,12,8,18,2]
# mydct={target_val:(i,j) for i in lst for j in lst if (i+j)==target_val}
# print(mydct)
pairs=set()
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==target_val:
            pairs.add((lst[i],lst[j]))
print(f"the pairs are {pairs}")


"""13. Create a function that validates whether a string is a valid email address using a simple regex (not full RFC)."""

"""14. Write a generator function that yields the first n prime numbers."""

def primes(k):
    if k==0:
        return 0
    else:

