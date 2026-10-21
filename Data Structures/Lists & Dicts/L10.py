"""Tuples

Tuple as Dictionary Key
Given a list of tuples representing (student, subject, marks):
records = [('Alice', 'Math', 85), ('Bob', 'Physics', 90), ('Alice', 'Math', 88), ('Charlie', 'Chemistry', 75)]
Create a dictionary where the key is a tuple (student, subject) and the value is the latest marks (if same key appears multiple times, keep the last one).
Sort Tuples with None Values
Given:
data = [(5, 2), (None, 8), (3, 1), (None, 4), (7, None)]
Sort the list of tuples by the first element (ascending). Treat None as the smallest possible value."""
from mesonbuild.cmake import language_map

records = [('Alice', 'Math', 85), ('Bob', 'Physics', 90), ('Alice', 'Math', 88), ('Charlie', 'Chemistry', 75)]
my_dict={ (i[0],i[1]):i[2] for i in sorted(records, key= lambda x:x[2],reverse = True) }
print(my_dict)

data = [(5, 2), (None, 8), (3, 1), (None, 4), (7, None)]
sorted_data = sorted(data, key=lambda x: float('-inf') if x[0] is None else x[0])
print(sorted_data)