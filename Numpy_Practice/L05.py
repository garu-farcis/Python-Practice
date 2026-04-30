"""Program 6.8: Find Mean, Variance and Standard Deviation of List Numbers
1. import math
2. def statistics(list_items):
3. mean = sum(list_items)/len(list_items)
4. print(f"Mean is {mean}")
5. variance = 0
6. for item in list_items:
7. variance += (item-mean)**2
8. variance /= len(list_items)
9. print(f"Variance is {variance}")
10. standard_deviation = math.sqrt(variance)
11. print(f"Standard Deviation is {standard_deviation}")
12. def main():
13. statistics([1, 2, 3, 4])
14. if __name__ == "__main__":
15. main()




Program 6.4: Write Python Program to Sort Numbers in a List in Ascending Order
Using Bubble Sort by Passing the List as an Argument to the Function Call
1. def bubble_sort(list_items):
2. for i in range(len(list_items)):
3. for j in range(len(list_items)-i-1):
4. if list_items[j] > list_items[j+1]:
5. temp = list_items[j]
6. list_items[j] = list_items[j+1]
7. list_items[j+1] = temp
8. print(f"The sorted list using Bubble Sort is {list_items}")
9. def main():
10. items_to_sort = [5, 4, 3, 2, 1]
11. bubble_sort(items_to_sort)
12. if __name__ == "__main__":
13. main()"""
import itertools
from itertools import combinations,permutations
names = ["Alan","Steven"]
def first_letter(x):
    return x[0]
for letter, names in itertools.groupby(names,first_letter):
    print(letter, list(names)) # names is a generator

from itertools import groupby,product

nums = [1, 3, 5, 2, 4, 6, 7]

# group by even/odd
for key, group in groupby(nums, key=lambda x: x % 2 == 0):
    print(key, list(group))

grouped=[(k,list(g)) for k,g in groupby(nums,key=lambda x:x%2==0)]
print(grouped)

nums = [1, 2, 3, 4]

for combo in combinations(nums, 3):
    print(combo)
features = ["age", "salary", "experience"]

for combo in combinations(features, 2):
    print(combo)
print(list(list(permutations([1,2,3], 2))))

from itertools import combinations_with_replacement

print(list(combinations_with_replacement([1,2,3], 2)))

a = [1, 2]
b = [10, 20]

for x, y in product(a, b):
    print(x + y,x,y)

a='aababcabcdabcde'
for key,group in groupby(a,key=lambda x:x[0]):
    print(key,list(group))
from collections import Counter

rrs= Counter(a)
print(rrs)
list_a=[i for i in a]
print(list_a)
freq={}
# max1=0
for each in list_a:
    freq[each]=freq.get(each,0)+1
max1=max(freq,key=freq.get)
print(freq,max1)

print(rrs.most_common(3))
print(rrs.most_common()[::-1])



