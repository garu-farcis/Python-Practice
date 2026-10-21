from random import choice,sample,shuffle
from string import punctuation

names = ['Joe','Bob','Sue','Sally']
current_player = choice(names)
print(current_player)
team = sample(names, 2)
print(team)
s='abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
for i in range(10000):
    print(choice(s), end='')
shuffle(names)
for p in names:
    print(p, 'it is your turn.')
teams = []
for i in range(0,len(names),2):
    teams.append([names[i], names[i + 1]])
print(teams)
s = 'Hi! This is a test.'
print(s.split())
for c in punctuation:
    s = s.replace(c, '')
print(s)
s1 = input('Enter a string: ')
for c in punctuation:
    s1 = s1.replace(c, '')
print(s1)
s1=s1.lower()
L=s1.split()
word = input('Enter a word: ')
print(word,'appears', L.count(word),'times')