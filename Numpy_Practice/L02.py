from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

cm = ChainMap(dict1, dict2)

print(cm)
print(cm.maps,'\n')
x=[(i,v) for i,v in enumerate(cm,start=0)]
print(x)
print('Kеys = {}'.format(list(cm.keys())))
print('Vаluеs = {}'.format(list(cm.values())))
print('еlеmеnts:')
for k, v in cm.items():
    print('{} = {}'.format(k, v))
print()