"""1. Write a function that takes a list of integers and returns a new list containing only the even numbers, each squared."""
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

""""""
