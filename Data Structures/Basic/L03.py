str = input("Enter string ")
print("no of chars ", len(str))
print("repeated 10 times ", str*10)
print("first char ", str[0])
print("last char ", str[-1])
print("first 3 char", str[:3])
print("last 3 char ", str[-3:])
print("reverse", str[::-1])
count= len(str)
if count>7:
    print("seventh char ", str[7])
else:
    print("Not longer than 7")
print("first n last char removed",str[1:-1])
print("upper case", str.upper())
str1 =''
for i in range(count):
    if 'a' in str[i]:
        str1 =str.replace(str[i],'e')
print("replaced string", str1)
str2 =''
for i in range(count):
    if 'a' in str[i]:
        str1 =str.replace(str[i],' ')
print("replaced string", str2)
