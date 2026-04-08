"""Let L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]. Use a list comprehension to
produce a list of the gaps between consecutive entries in L. Then find the maximum gap size
and the percentage of gaps that have size 2."""

L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
L1 =[ (L[i+1]-L[i]) for i in range(len(L)-1)]
print(L1)
maxval=max(L1)
print(maxval)
counti=0
L2 =[ i for i in L1 if i==2]
print(L2)
percen = (len(L2) / len(L1)) * 100
print(percen)