str = input('Enter a string: ')
articles=['a','an','the']
count =0
L = str.split()
value = [i for i in str if i in articles]
print(len(value))
