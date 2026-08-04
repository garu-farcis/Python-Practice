"""1. Write a function that takes a list of integers and returns a new list containing only the even numbers, each squared."""
from functools import lru_cache

from mypy.types import NONE_TYPE


def mylist(lst):
    print(f"original list is {lst}")
    newlst=[i for i in lst if i%2==0]
    res= [i*i for i in newlst]
    return res
mlist=[2,4,3,5,6,3,44,54,65,67,676,44,77,57]
res=mylist(mlist)
print(res)


"""2. Write a function that counts the frequency of each alphabetic character in a string (ignore case and non-letters)."""
from collections import defaultdict
def calfreq(mystring):
    print(f"original string is {mystring}")
    freq=defaultdict(int)
    charss=list(mystring)
    for each in charss:
        freq[each]+=1
    return freq
strs="Hello World You are beautiful"
val=calfreq(strs)
print(val)

"""3. Implement a function that flattens a nested list of arbitrary depth into a single flat list."""
def flatten(lst):
    print(f"original list is {lst}")
    flat=[]
    for i in lst:
        if isinstance(i,list):
            flat.extend(flatten(i))
        else:
            flat.append(i)
    return flat

mylst=[[1,2,[3,4]],2,3,[3,4]]
res=flatten(mylst)
print(f"flattened list is {res}")

"""4. Write a function that finds the second-largest unique number in a list. Return None if it does not exist."""
def secondlarg(lst):
    print(f"original list is {lst}")
    dups=[]
    unique=[]
    for each in lst:
        if each not in dups:
            unique.append(each)
        else:
            dups.append(each)
    unique.sort(reverse=False)
    print(unique)
    return unique[-2]

lists=[2,3,4,35,65,76,54,35,77,342,87]
res=secondlarg(lists)
print(res)

"""5. Create a class BankAccount with deposit, withdraw, and get_balance methods. Raise ValueError on insufficient funds or non-positive amounts."""

class BankAccount:
    def __init__(self,balance=0):
        self._balance=balance
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("amount cannot be zero")
        else:
            self._balance+=amount
        return self._balance
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        else:
            self._balance-=amount
        return self._balance

    def get_balance(self):
        return self._balance

acc=BankAccount(800)
print(acc.deposit(900))
print(acc.withdraw(1000))
print(acc.get_balance())

"""6. Write a function that groups a list of words by their first letter into a dictionary of lists."""

def groupslsts(mystr):
    print(f"original string is {mystr}")
    groups=defaultdict(list)
    for each in mystr:
        groups[each[0]].append(each)
    return groups

cases=["Apple", "Banana", "Apricot", "Cherry", "Avocado"]
res=groupslsts(cases)
print(res)

"""7. Implement a recursive Fibonacci function with memoization using functools.lru_cache."""
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(val):
    if val<2:
        return val
    return fib(val-1) +fib(val-2)
x=fib(10)
print(x)