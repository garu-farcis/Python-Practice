from math import log
n =int(input("Enter limit: "))
range_num= float(1/n)
print(range_num)
value =0
for i in range(1,n+1):
    value = float(value + (1/i))
print(value)
print(log(n))
fin_val =value -log(n)
print(fin_val)
