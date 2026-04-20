"""Tuples

Tuple Frequency Counter
Given a list of tuples:
tuples_list = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
Write code to return a dictionary showing how many times each tuple appears (frequency count).
Sort Tuples by Sum
Given a list of tuples:
data = [(1, 3), (4, 1), (2, 5), (7, 2), (3, 6)]
Sort the list of tuples in descending order based on the sum of elements in each tuple."""

tuples_list = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
unique_lst=[]
dups =[]
c=0
for i in tuples_list:
    if i not in unique_lst:
        unique_lst.append(i)
freq = {}

for t in tuples_list:
    freq[t] = freq.get(t, 0) + 1

print('frequencies',freq)
print(unique_lst)
data = [(1, 3), (4, 1), (2, 5), (7, 2), (3, 6)]
data.sort()
my_d= data[::-1]
print(my_d)
my_dict={ i:sum(i) for i in my_d}
print(my_dict)
print(sorted(my_dict.items(),key =lambda x: x[1], reverse = True ))

