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