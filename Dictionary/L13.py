"""
1. Given a nested list:

Pythonmatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Use a nested list comprehension to flatten it into a single list [1, 2, 3, 4, 5, 6, 7, 8, 9].

2. Using a dictionary comprehension, create a dict char_count from the list sentences = ["hello world", "python is fun", "hello again"] where each key is a unique character (lowercase) across all sentences and the value is its total count.
3. Given:

Pythondata = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 25}]
Use a dictionary comprehension + groupby logic (or manual logic) to create a dict where the key is age and the value is a list of names of people with that age.

4. Write a single list comprehension that takes lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and produces a list of tuples: [(1, 'odd'), (2, 'even'), (3, 'odd'), ...].
5. Given two dictionaries:

Pythond1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 4, "d": 5}
Merge them into merged such that:

 If a key exists in both, keep the sum of values
Use only a dictionary comprehension (no |= or update).


6. Given students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)], use a list comprehension + sorted to create a list of names sorted by score in descending order.
7. Using a dictionary comprehension, invert the following dictionary (swap keys and values). Handle duplicate values by storing them as a list:

Pythonoriginal = {"a": 1, "b": 2, "c": 1, "d": 3}

8. Given a list of strings:

Pythondata = ["apple:5", "banana:8", "cherry:3", "date:10"]
Use one dictionary comprehension to create a dict where the fruit name is the key and the number (as int) is the value.

9. Create a nested dictionary comprehension that produces:

Python{
    1: [1],
    2: [1, 2],
    3: [1, 2, 3],
    ...
    5: [1, 2, 3, 4, 5]
}
(keys from 1 to 5, values = list of numbers from 1 to the key).

10. Challenge: Given transactions = [("buy", 100), ("sell", 50), ("buy", 200), ("sell", 75)], write one dictionary comprehension that returns:

Python{"buy": 300, "sell": 125}
(sum the amounts for each type)."""
import pprint
from itertools import zip_longest

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
fla_t=[j for m in matrix for j in  m ]
pprint.pprint(fla_t)

from collections import defaultdict
sentences = ["hello world", "python is fun", "hello again"]

char_count = {char: sum(sentence.lower().count(char) for sentence in sentences)
              for sentence in sentences
              for char in sentence.lower()}
pprint.pprint(dict(char_count))

char_count = {k: v for k, v in char_count.items()}

print(char_count)

data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Charlie", "age": 25}]

result =[]
for item in data:
    print(item)
    for i in item.items():
        print(i)
        result.append(i)
print(result)
age_l =[result[i] for i in range(len(result)) if i%2!=0]
name_l =[result[i] for i in range(len(result)) if i%2==0]
print(name_l)
print(age_l)
a ='age'
n ='name'
flat_age =[j for m in age_l for j in m if j !=a]
print(flat_age)
flat_name =[j for m in name_l for j in m if j!=n ]
print(flat_name)
my_dict ={k:v for k,v in zip_longest(flat_age, flat_name, fillvalue='')}
print('jhgjhff mjbmgm   ', my_dict)
my_dic=defaultdict(list)
for k,v in my_dict.items():
    my_dic[k].append(v)
print(my_dic)

from collections import defaultdict

grouped = defaultdict(list)
d =defaultdict(list)
d1=defaultdict(int)
d2=defaultdict(int)

for item in data:
    grouped[item["age"]].append(item["name"])
    d["name"].append(item["name"])
    d["age"].append(item["age"])
    d1[item["name"]]+=1
    d2[item["age"]]+=1


print("nbvsdnsvmfvmvfm     ", d2)
print('jhgsjdhghgsckfjs     ', d1)
print('hello  ',dict(d))

print(dict(grouped))
# pprint.pprint(names)
# pprint.pprint(ages)
s = "hello"
s.split()
print(len(s))

d = defaultdict(lambda: defaultdict(int))

d["A"]["x"] += 1

print(d)


words = ["hi", "hello","hi","hi"]
len_words = [len(w) for w in words]
print(len_words)
w_dict ={k:len(k) for k in words}
print(w_dict)
dup_w=[(w,words.count(w)) for w in set(words) if words.count(w)>1]
print(dup_w)
nums = [1, 2, 2, 3, 3, 3]
count_dict = {x: nums.count(x) for x in nums}
print(count_dict)
dups = {k: v for k, v in count_dict.items() if v > 1}
print(dups.keys())
s = "banana"
L_s =[s[i] for i in range(len(s))]
print(s)
L ={ ch:i for i, ch in enumerate(L_s)}
print(L)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_L =[((i,'even') if i%2==0 else (i,'odd') )for i in lst ]
print(my_L)

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 4, "d": 5}

merged = {
    k: d1.get(k, 0) + d2.get(k, 0)
    for k in d1.keys() | d2.keys()
}

print(merged)

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
res = [k for k,v in sorted(students, key=lambda x:x[1],reverse=True) ]
print(res)

original = {"a": 1, "b": 2, "c": 1, "d": 3}
myd= { v:k for k,v in original.items() }
print(myd)
dups =[i for i in original if original[i] != original[i]]
print(dups)