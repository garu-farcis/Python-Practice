"""
1.Create a list fruits containing ["apple", "banana", "cherry", "date"]. Then append "elderberry" and print the final list.
2.Given nums = [10, 20, 30, 40, 50], write code to access and print the 3rd element (0-based indexing) and the last element using negative indexing.
3.Create an empty dictionary student. Add the keys "name": "Alice", "age": 20, and "grade": "A". Then print the dictionary.
4.Given my_dict = {"a": 1, "b": 2, "c": 3}, write code to:
Change the value of key "b" to 99
Remove the key "c"
Print the updated dictionary

5.Write a for-loop to create a list squares that contains the squares of numbers from 1 to 10 (i.e., [1, 4, 9, ..., 100]).
6.Given lst = ["cat", "dog", "bird", "fish"], write code to convert it into a dictionary where each string is a key and its length is the value (using a loop).
7.Predict the output of the following code:Pythond = {"x": 10, "y": 20}
d["z"] = d.get("x") + d.get("y")
print(d)
8.Create a list evens containing all even numbers from 0 to 20 inclusive using the range() function. Then convert this list into a dictionary where the index becomes the key and the number becomes the value (use enumerate).
9.Given two lists:Pythonkeys = ["red", "green", "blue"]
values = ["#FF0000", "#00FF00", "#0000FF"]Write code (without comprehensions) to create a dictionary color_dict using zip() and dict().
10. Given data = {"a": 5, "b": 3, "c": 8}, write code to create a list sorted_keys that contains the keys sorted by their values in ascending order (use sorted with a key function)."""

fruits=["apple","banana","cherry","date"]
extra= ["elderberry"]
print(fruits + extra)

nums=[10,20,30,40,50]
print(nums[2],nums[-1])

students={}
students["name"]="Alice"
students["age"]=20
students["grade"]="A"
print(students.items())

my_dict={'a':1,'b':2,'c':3}
my_dict['b']=99
del my_dict['c']
print(my_dict)

L =[i**2 for i in range(1,11)]
print(L)

lst =['cat','dog','bird','fish']
my_dict1={s:len(s) for s in lst}
print(my_dict1)

d= {'x':10,'y':20}
d['z'] = d.get('x') + d.get('y')
print(d)

L1 =[i for i in range(1,21) if i%2==0]
print(L1)
indic =[i for i in range(len(L1)+1)]
print(indic)
for i,j in enumerate(L1):
    print(i,j)
print(dict(zip(indic,L1)))


keys =['red','green','blue']
values=['#FF0000','#00FF00','#0000FF']
for k,v in zip(keys,values):
    print(k,v)
print(dict(zip(keys,values)))

data ={'a':5,'b':3,'c':8}
n_d =data.keys()
nd_item = list(data.items())
print(n_d)
print(nd_item)
vals = data.values()
print(vals)
sorted_keys = [k for k, v in sorted(data.items(), key=lambda x: x[1])]
print(sorted_keys)
