items = [

]

MIN_SIZE = 50
MAX_SIZE = 51

items.sort(key=lambda x: x[1], reverse=True)

bins = []  # each bin: {"items": [...], "total": 0}

for name, size in items:
    placed = False
    for b in bins:
        if b["total"] + size <= MAX_SIZE:
            b["items"].append((name, size))
            b["total"] += size
            placed = True
            break
    if not placed:
        bins.append({"items": [(name, size)], "total": size})

for i, b in enumerate(bins, 1):
    print(f"Bin {i}: {b['total']:.2f} GB — {[n for n,_ in b['items']]}")