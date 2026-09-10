"""Write a function that receives a list of tuples (name, age, city) and returns a nested dictionary grouped first by city,
 then by age range ("young" if age < 30, "adult" otherwise), containing lists of names.
Sample Input: [("Alice", 25, "NY"), ("Bob", 35, "NY"), ("Charlie", 22, "LA"), ("Diana", 40, "LA")]
Sample Output: {"NY": {"young": ["Alice"], "adult": ["Bob"]}, "LA": {"young": ["Charlie"], "adult": ["Diana"]}}"""

my_lst=[("Alice", 25, "NY"), ("Bob", 35, "NY"), ("Charlie", 22, "LA"), ("Diana", 40, "LA")]
from collections import defaultdict

def calc(my_tup):
    my_dict=defaultdict(list)
    for val in my_tup:
        my_dict[val[2]].append([val[0],val[1]])
    print(my_dict)
    res=defaultdict(lambda: defaultdict(list))
    val=defaultdict(list)
    for k,v in my_dict.items():
        for i,j in v:
            if j>30:
                res[k]['adult'].append(j)
            else:
                res[k]['young'].append(j)
    print(res)


x=calc(my_lst)
