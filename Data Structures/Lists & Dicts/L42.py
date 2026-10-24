"""Scenario: You receive multiple sorted CSV partitions (by primary key) and need to produce one globally sorted stream without loading everything into memory at once.
Problem: Write a generator that merges multiple sorted iterables of (key, value) pairs and yields them in sorted order.
Sample Input:
Pythonpart1 = [(1, "a"), (4, "d"), (7, "g")]
part2 = [(2, "b"), (5, "e")]
part3 = [(3, "c"), (6, "f")]
Sample Output (as list for illustration):
Python[(1, "a"), (2, "b"), (3, "c"), (4, "d"), (5, "e"), (6, "f"), (7, "g")]
"""
part1 = [(1, "a"), (4, "d"), (7, "g")]
part2 = [(2, "b"), (5, "e")]
part3 = [(3, "c"), (6, "f")]
