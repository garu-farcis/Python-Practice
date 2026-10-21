"""1. Given a list of integers, return a new list containing only the elements that appear exactly twice, preserving the order of their first occurrence.
Sample Input: [4, 2, 4, 5, 2, 3, 4, 5, 1]
Sample Output: [ 2, 5]"""


list_int=[4, 2, 4, 5, 2, 3, 4, 5, 1]
my_list=[]
for i in list_int:
    if list_int.count(i) == 2 and i not in my_list:
        my_list.append(i)
print(f"new list is {my_list}")
