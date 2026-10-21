"""Given a list of strings like data = ["apple:5", "banana:8", "cherry:3"], use one dictionary comprehension to parse
 it into {'apple': 5, 'banana': 8, 'cherry': 3} (convert values to int."""

data = ["apple:5", "banana:8", "cherry:3"]
data_set = [i.split(":") for i in data]
print(data_set)
my_dict ={ k:v for k,v in data_set }
print(my_dict)