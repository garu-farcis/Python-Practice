"""Challenge: Given transactions = [("buy", 100), ("sell", 50), ("buy", 200), ("sell", 75)], write one dictionary comprehension that returns:

Python{"buy": 300, "sell": 125}
(sum the amounts for each type)."""
transactions = [("buy", 100), ("sell", 50), ("buy", 200), ("sell", 75)]
my_dict ={k:sum(v for k2, v in transactions if k2 == k)  for k in {k for k, _ in transactions }}
print(my_dict)
my_dict1 ={k:[v for k2, v in transactions if k2 == k]  for k in {k for k, _ in transactions }}
print(my_dict1)


