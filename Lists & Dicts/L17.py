"""Find Duplicate Files by Content
Given a list of file paths with content:

files = [
    "root/a 1.txt(abcd) 2.txt(efgh)",
    "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)",
    "root 5.txt(xyz)"
]

Return groups of file paths that have identical content.
Expected output:

[
  ["root/a/1.txt", "root/c/3.txt"],
  ["root/a/2.txt", "root/c/d/4.txt"]
]"""

files = [
    "root/a 1.txt(abcd) 2.txt(efgh)",
    "root/c 3.txt(abcd)",
    "root/c/d 4.txt(efgh)",
    "root 5.txt(xyz)"
]


from collections import defaultdict

content_map = defaultdict(list)

for entry in files:
    parts = entry.split()
    print(parts)
    folder = parts[0]

    for file in parts[1:]:
        name, content = file.split('(')

        content = content[:-1]  # remove closing ')'
        print(content)

        path = folder + "/" + name
        content_map[content].append(path)

result = list(content_map.values())

print(result)
