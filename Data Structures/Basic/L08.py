num_right = 0
# Question 1
print('What is the capital of France?', end=' ')
guess = input()
if guess.lower()=='paris':
    print('Correct!')
    num_right+=1
else:
    print('Wrong. The answer is Paris.')
print('You have', num_right,'out of 1 right')
#Question 2
print('Which state has only one neighbor?', end=' ')
guess = input()
if guess.lower()=='maine':
    print('Correct!')
    num_right+=1
else:
    print('Wrong. The answer is Maine.')
print('You have', num_right,'out of 2 right,')