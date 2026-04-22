"""Sets
Longest Consecutive Sequence
Given:
nums = [100, 4, 200, 1, 3, 2]
Find the length of the longest consecutive elements sequence.
Expected output: 4 (sequence: [1,2,3,4])
(Must run in O(n) using a set)
Subset Check with Multiple Sets
Given a list of sets:
sets_list = [{1,2}, {1,2,3,4}, {2,3}, {1,2,3}]
Find all sets that are subsets of at least one other set in the list."""
from collections import defaultdict
nums = [100, 4, 200, 1, 3, 2]
my_lst=set(nums)
print(my_lst)
seq=[]
seq2=[]
long =0
for i in my_lst:

    if i-1 not in my_lst:
        current =i
        length =1
        seq=[i]

        while current+1 in my_lst:
            current+=1
            length+=1
            seq.append(current)
        long = max(long, length)
        seq2.append(seq)


print(seq2[0])
print(seq2)
print(long)

sets_list = [{1,2}, {1,2,3,4}, {2,3}, {1,2,3}]
results=[]
for i in range(len(sets_list)):
    for j in range(len(sets_list)):
        if i != j and sets_list[i].issubset(sets_list[j]):
            results.append(sets_list[i])
            break
print(results)

