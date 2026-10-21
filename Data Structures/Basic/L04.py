str =input("enter a sentence")
x = len(str)
count=0
for i in range(x):
    if ' ' in str[i]:
        count+=1
print("no of words", count+1)