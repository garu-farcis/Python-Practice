deck = [{'value':i,'suit':c}
        for c in ['spades','clubs','hearts','diamonds']
        for i in range(2,15)]
print(deck)
d = dict([('A',100),('B',300)])
print(d)
words ='hbmbmxsbvmgkrfjgkjwgekfk'
d2 = {s : len(s) for s in words}
print(d2)

from string import punctuation
text = 'a a a an an the fgr dfs hsg'
t =text.split()
print(t)
text = text.lower()
for p in punctuation:
    text = text.replace(p,'')
words = text.split()
print(words)
d = {}
for w in words:
    if w in d:
        d[w] = d[w] + 1
    else:
        d[w] = 1
items = list(d.items())
items.sort()
for i in items:
    print(i)
d ={s for s in text}
print(d)
