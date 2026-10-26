"""Scenario: A multi-GB CSV cannot fit in memory. You need to compute a global sum of a column while processing in chunks.
Problem: Write a function that reads a CSV in chunks of size chunksize, sums a numeric column, and returns the total. Handle the header correctly.
Sample Input (conceptual):
Python#
file content:
# id,value
# 1,10
# 2,20
# 3,30
chunksize = 2
Sample Output:
Python
60"""
import os
import pandas as pd
def read_chunks(filepath,chunksize):
    fd = os.open(filepath, os.O_RDONLY)
    readBytes=os.read(fd,chunksize)
    df=pd.DataFrame(readBytes)
    total=df['value'].sum()
    return total
filep="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/students.csv"
chunks=2
res=read_chunks(filep,chunks)