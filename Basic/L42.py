x,y,z = 1,2,3
x,y,z = y,z,x
print(x,y,z)
words = 'hwdszjjjjzzzjzzz'
words = words.split()
L= [w for w in words if w[4]=='z' and len(w) > 4]
print(L)
bill = 23.60
tip = 23.60*.25
print('Tip: ${:.2f}, Total: ${:.3f}'.format(tip, bill+tip))
print('{:3d}'.format(2))
print('{:<d}'.format(25))
print('{:^5d}'.format(138))
print('{:,d}'.format(1000000))
print('{:^10s}'.format('Hi'))
print('{:^10s}'.format('there!'))
print('{:>6s}'.format('Hi'))
print('{:>6s}'.format('There'))
print('{:<6s}'.format('There'))
print('{:^6s}'.format('There'))
for i in range(1,11):
    for j in range(1,11):
        print('{:3d}'.format(i*j), end=' ')
    print()
for x in range(-50,51):
    for y in range(-50,51):
        if 2*x+3*y==4 and x-y==7:
            print(x,y)

L3=''.join([c*i for c in 'Python' for i in range(1,7)])
print(L3)
L4 = ''.join([c * i for c in 'Python' for i in range(1, 7)])
print(L4)