"""Given a list of strings:

Python

data = ["apple:5", "banana:8", "cherry:3", "date:10"]
Use one dictionary comprehension to create a dict where the fruit name is the key and the number (as int) is the value."""

data = ["apple:5", "banana:8", "cherry:3", "date:10"]
my_d =[i.split(':') for i in data ]
print(my_d)
my_dict ={k:int(v) for k,v in my_d }
print(my_dict)