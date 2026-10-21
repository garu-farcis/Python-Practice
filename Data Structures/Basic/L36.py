"""This exercise is useful in creating a Memory game. Randomly generate a 6 ×6 list of assorted
characters such that there are exactly two of each character. An example is shown below.
@ 5 # A A !
5 0 b @ $ z
$ N x ! N z
0 - + # b :
- : + c c x"""
import random

alph = 'abcdefghijklmnopqrstuvwxyz'
chars = random.sample(alph, 18)
pairs = chars * 2
random.shuffle(pairs)
s = [pairs[i:i+6] for i in range(0, 36, 6)]

print(s)