"""
1. Given a nested list of integers (lists can contain integers or other lists), write a function that returns the sum of all integers.
Sample Input: [1, [2, [3, 4], 5], 6]
Sample Output: 21

2. Write a function that flattens a nested dictionary into a single-level dictionary using dot notation for keys.
Sample Input: {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
Sample Output: {"a": 1, "b.c": 2, "b.d.e": 3}

3. Given a list of nested dictionaries representing employees, return a new list containing only employees who work in a specific department.
Sample Input:
employees = [
    {"name": "Alice", "info": {"dept": "Engineering", "level": 3}},
    {"name": "Bob", "info": {"dept": "HR", "level": 2}},
    {"name": "Charlie", "info": {"dept": "Engineering", "level": 4}}
]
department = "Engineering"
Sample Output: [{"name": "Alice", "info": {"dept": "Engineering", "level": 3}}, {"name": "Charlie", "info": {"dept": "Engineering", "level": 4}}]

4. Write a function that deeply merges two nested dictionaries. If a key exists in both and both values are dictionaries, merge them recursively. Otherwise, the second dictionary’s value overwrites the first.
Sample Input:
d1 = {"a": 1, "b": {"c": 3, "d": 4}}
d2 = {"b": {"c": 5, "e": 6}, "f": 7}
Sample Output: {"a": 1, "b": {"c": 5, "d": 4, "e": 6}, "f": 7}

5. Given a nested list that represents a matrix, write a function that returns the transpose of the matrix.
Sample Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Sample Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

6. Write a function that takes a nested dictionary and a list of keys, and returns the value at that nested path. Return None if the path does not exist.
Sample Input:
data = {"user": {"profile": {"name": "Alice", "age": 30}}}
keys = ["user", "profile", "name"]
Sample Output: "Alice"

7. Given a list of nested lists, write a function that returns the maximum depth of nesting.
Sample Input: [1, [2, [3, [4]]], 5]
Sample Output: 4

8. Write a function that converts a nested list of key-value pairs into a nested dictionary.
Sample Input: [["a", [["b", 2], ["c", 3]]], ["d", 4]]
Sample Output: {"a": {"b": 2, "c": 3}, "d": 4}

9. Given a deeply nested dictionary, write a function that replaces all values of a specific key with a new value, no matter how deep the key appears.
Sample Input:
data = {"a": 1, "b": {"x": 10, "y": {"x": 20}}, "x": 5}
key = "x"
new_value = 99
Sample Output: {"a": 1, "b": {"x": 99, "y": {"x": 99}}, "x": 99}

10. Write a function that takes a nested structure of lists and dictionaries and returns a list of all leaf values (values that are not lists or dictionaries).
Sample Input: {"a": [1, {"b": 2, "c": [3, 4]}, 5], "d": 6}
Sample Output: [1, 2, 3, 4, 5, 6]
"""

# 1. Given a nested list of integers (lists can contain integers or other lists),
# write a function that returns the sum of all integers.
# Sample Input: [1, [2, [3, 4], 5], 6]
# Sample Output: 21


def my_recur(lst):
    flat_list=[]
    for each in lst:
        if isinstance(each,list):
            flat_list.extend(my_recur(each))
        else:
            flat_list.append(each)
    return flat_list


my_lst = [1, [2, [3, 4], 5], 6]
recur=my_recur(my_lst)
print(sum(recur))