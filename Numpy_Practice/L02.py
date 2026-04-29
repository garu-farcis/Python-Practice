from collections import ChainMap
from collections import defaultdict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

cm = ChainMap(dict1, dict2)

print(cm)
for key, value in cm.items():
    print(key, value)
print(cm.maps,'\n')
dict2['d'] = 7
print(cm.maps,'\n')
x=[(i,v) for i,v in enumerate(cm,start=0)]
print(x)
print('dаy3 in rеs: {}'.format(('b' in cm)))
d =defaultdict(list)
print('Kеys = {}'.format(list(cm.keys())))
print('Vаluеs = {}'.format(list(cm.values())))
print('еlеmеnts:')

for i in cm.maps:
    if isinstance(i,dict):
        for k,v in i.items():
            d[k].append(v)
print('using defaultdict',d)
for k, v in cm.items():
    print('{} = {}'.format(k, v))
print()

