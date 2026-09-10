"""Implement a function that takes a nested list (lists can contain integers or other lists) and returns a flattened list of all integers in order.
Sample Input: [1, [2, [3, 4], 5], 6, [7, 8]]
Sample Output: [1, 2, 3, 4, 5, 6, 7, 8]"""

intrevals= [1, [2, [3, 4], 5], 6, [7, 8]]
for i in intrevals:
    def rec_inte(my_list):
        flat_list=[]
        for i in my_list:
            if isinstance(i, list):
                 flat_list.extend(rec_inte(i))
            else:
                flat_list.append(i)

        return flat_list

x=rec_inte(intrevals)
print(x)