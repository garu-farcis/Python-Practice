str =input("enter a word")
x = len(str)
count=0
for i in range(x):
    if str[i] in "aeiou":
        count+=1
if count>=1:
    print("vowels are present")
else:
    print("vowels are not present")
print("no of vowels", count)