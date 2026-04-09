"""This exercise is useful in creating a Memory game. Randomly generate a 6 ×6 list of assorted
characters such that there are exactly two of each character. An example is shown below.
@ 5 # A A !
5 0 b @ $ z
$ N x ! N z
0 - + # b :
- : + c c x"""

from random import choice
alphabet ='abcdefghijklmnopqrstuvwxyz'
s = ''.join([choice(alphabet) for i in range(1000)])
print(s)