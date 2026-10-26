"""Scenario: You receive multiple sorted CSV partitions (by primary key) and need to produce one globally sorted stream without loading everything into memory at once.
Problem: Write a generator that merges multiple sorted iterables of (key, value) pairs and yields them in sorted order.
Sample Input:
Pythonpart1 = [(1, "a"), (4, "d"), (7, "g")]
part2 = [(2, "b"), (5, "e")]
part3 = [(3, "c"), (6, "f")]
Sample Output (as list for illustration):
Python[(1, "a"), (2, "b"), (3, "c"), (4, "d"), (5, "e"), (6, "f"), (7, "g")]
"""

from collections import defaultdict
def partition_prob(list1,list2,list3)->list:
    my_list=[]
    # for i in list1:
    #     my_list.append(i)
    # for i in list2:
    #     my_list.append(i)
    # for i in list3:
    #     my_list.append(i)
    my_list = list1 + list2 + list3
    my_dict=defaultdict(list)
    for k,v in my_list:
        my_dict[k].append(v)
    for key in sorted(my_dict.keys()):
        for v in my_dict[key]:
            yield (k,v)



part1 = [(1, "a"), (4, "d"), (7, "g")]
part2 = [(2, "b"), (5, "e")]
part3 = [(3, "c"), (6, "f")]
val=partition_prob(part1,part2,part3)
print(val)
