"""Write a program that finds all pairs of six-digit palindromic numbers that are less than 20
apart. One such pair is 199991 and 200002"""


my_list = []

for i in range(100000, 1000000):
    digits = []
    for ch in str(i):
        digits.append(int(ch))
    my_list.append(digits)


my_list = [list(map(int, str(i))) for i in range(100000, 1000000)]
L=[i for i in my_list if i==i[::-1]]
print(L)