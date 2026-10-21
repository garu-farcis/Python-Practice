from random import randint
# secret_num = randint(1,10)
# guess = 0
# while guess != secret_num:
#     guess = eval(input('Guess the secret number: '))
print('You finally got it!')
L = list('1234566333')
for i in range(1,10001):
    s = str(i)
    if s==s[::-1]:
        print(s)

birthday ='January 1, 1991'
year = int(birthday[-4:])
print('You are', 2010-year,'years old.')
num = 34
digit = str(num)
answer = int(digit[0]) + int(digit[1])
L1 =[[j for i in range (5)] for j in range (5)]
print(L1)
val =[sum(L1[i]) for i in range(5)]
print(val)

