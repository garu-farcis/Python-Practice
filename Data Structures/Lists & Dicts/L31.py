"""Implement a function that takes a nested list (lists can contain integers or other lists) and returns a flattened list of all integers in order.
Sample Input: [1, [2, [3, 4], 5], 6, [7, 8]]
Sample Output: [1, 2, 3, 4, 5, 6, 7, 8]"""
from collections import defaultdict

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

# 10. Given a dictionary of item prices and a list of purchased items
# (with possible duplicates), return the total cost after applying a discount rule: every third identical item is free.
# Sample Input: prices = {"apple": 2, "banana": 1, "orange": 3}, cart = ["apple", "apple", "apple", "banana", "orange", "orange"]
# Sample Output: 9

prices = {"apple": 2, "banana": 1, "orange": 3}
cart = ["apple", "apple", "apple", "banana", "orange", "orange"]

cart_count=defaultdict(int)
for c in cart:
    cart_count[c]+=1
print(cart_count)
total_sales=defaultdict(list)
for fruit,price in prices.items():
    cnt=cart_count[fruit]
    if cnt%3==0:
        count_manythree=cnt//3
        count=cnt-count_manythree
        total_sales[fruit].append(price * count)
    else:
        total_sales[fruit].append(price*cnt)
print(total_sales)
total_rev=[]
for i in total_sales.values():
    total_rev=total_rev+i
print(sum(total_rev))
