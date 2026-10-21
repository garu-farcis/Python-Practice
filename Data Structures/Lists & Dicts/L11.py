"""Dictionaries

Nested Dictionary Flattening
Given a nested dictionary:
nested = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': {'f': {'g': 4}}}
Flatten it into a single-level dictionary with dot notation for keys.
Expected: {'a': 1, 'b.c': 2, 'b.d': 3, 'e.f.g': 4}
Dictionary from Two Lists with Default
Given two lists:
keys = ['name', 'age', 'city', 'country']
values = ['Alice', 25, 'New York']
Create a dictionary from these two lists. If a key has no corresponding value, assign None as default.
Merge List of Dictionaries
Given:
data = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5, 'd': 6}]
Merge all dictionaries into one. If the same key appears in multiple dicts, sum their values."""
from collections import defaultdict
nested = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': {'f': {'g': 4}}}
d =defaultdict(list)
def flatten_dict(d, parent_key='', sep='.'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep))
        else:
            items[new_key] = v
    return items


nested = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': {'f': {'g': 4}}}

print(flatten_dict(nested))

