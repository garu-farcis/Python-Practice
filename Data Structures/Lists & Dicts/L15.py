"""Dictionaries

Nested Dictionary Flattening
Given a nested dictionary:

data = {
    "a": 1,
    "b": {"c": 2, "d": {"e": 3}}
}

Flatten it so that nested keys are joined by a dot (.).
Expected output: {'a': 1, 'b.c': 2, 'b.d.e': 3}

Invert a Dictionary with Duplicate Values
Given:
data = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
Invert the dictionary so that values map to a list of keys.
Expected output: {1: ['a', 'c'], 2: ['b', 'd'], 3: ['e']}
LRU Cache Simulation (Basic)
Simulate a simple LRU (Least Recently Used) cache with capacity = 3 using a dictionary.
Process operations:
["put a", "put b", "put c", "get a", "put d"]
Show final state of cache keys (least recent → most recent)"""
from collections import defaultdict
data = {
    "a": 1,
    "b": {"c": 2, "d": {"e": 3}}
}

def flat_dict(d,p_key='',sep='.'):
    result = {}
    for k,v in d.items():

        new_k=f"{p_key}{sep}{k}" if p_key else k
        if isinstance(v,dict):
            result.update(flat_dict(v,new_k,sep))
        else:
            result[new_k]=v
    return result


print(flat_dict(data))

data = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
d=defaultdict(list)
for k,v in data.items():
    d[v].append(k)
print(d)