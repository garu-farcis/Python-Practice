"""Let L be a list of strings. Write list comprehensions that create new lists from L for each of the
following.
(a) A list that consists of the strings of L with their first characters removed
(b) A list of the lengths of the strings of L
(c) A list that consists of only those strings of L that are at least three characters long"""


str = input("Enter a string: ")
L = str.split()
print(L)
L_rem= [m[1:] for m in L]
print(L_rem)
print(len(L_rem))
L_lettre=[i for i in L if len(i)==3]
print(L_lettre)


