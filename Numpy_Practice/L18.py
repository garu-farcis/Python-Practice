import numpy as np
from io import StringIO
data = "1, 2, 3\n4, 5, 6"
x= np.genfromtxt(StringIO(data), delimiter=",")
print(x)
data = "  1  2  3\n  4  5 67\n890123  4"
print(np.genfromtxt(StringIO(data), delimiter=3))
data = "123456789\n   4  7 9\n   4567 9"
print(np.genfromtxt(StringIO(data), delimiter=(4, 3, 2)))
data = "1, abc , 2\n 3, xxx, 4"
# Without autostrip
print(np.genfromtxt(StringIO(data), delimiter=",", dtype="|U5"))
# With autostrip
print(np.genfromtxt(StringIO(data), delimiter=",", dtype="|U5", autostrip=True))
ata = """#
# Skip me !
# Skip me too !
1, 2
3, 4
5, 6 #This is the third line of the data
7, 8
# And here comes the last line
9, 0
"""
print(np.genfromtxt(StringIO(ata), comments="#", delimiter=","))

