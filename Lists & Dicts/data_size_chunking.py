import re

x = ()

result = {}

for item in x:
    size, filename = item.split(maxsplit=1)
    result[filename.lower()] = size

print(result)


# --- convert size strings like '9.9M', '1.2G', '800K' to GB (float) ---
def to_gb(size_str):
    match = re.match(r'([\d.]+)\s*([KMGTkmgt])', size_str.strip())
    if not match:
        raise ValueError(f"Can't parse size: {size_str!r}")
    num = float(match.group(1))
    unit = match.group(2).upper()
    factors = {'K': 1/1024**2, 'M': 1/1024, 'G': 1, 'T': 1024}
    return num * factors[unit]

items_gb = [(name, to_gb(size)) for name, size in result.items()]

# --- sanity check ---
total = sum(size for _, size in items_gb)
print(f"Total: {total:.2f} GB, ideal bin count: ~{total/50:.1f}\n")

# --- Best Fit Decreasing bin packing ---
MIN_SIZE = 49
MAX_SIZE = 52  # slight tolerance around 50-51

items_gb.sort(key=lambda t: t[1], reverse=True)
bins = []
for name, size in items_gb:
    best_bin, best_remaining = None, None
    for b in bins:
        remaining = MAX_SIZE - (b['total'] + size)
        if remaining >= 0 and (best_remaining is None or remaining < best_remaining):
            best_bin, best_remaining = b, remaining
    if best_bin:
        best_bin['items'].append((name, size))
        best_bin['total'] += size
    else:
        bins.append({'items': [(name, size)], 'total': size})

# --- output ---
for i, b in enumerate(bins, 1):
    flag = "" if MIN_SIZE <= b['total'] <= MAX_SIZE else "  <-- outside target range"
    print(f"Bin {i}: {b['total']:.2f} GB{flag}")
    for name, size in b['items']:
        print(f"   {size:6.2f} GB  {name}")
    print()