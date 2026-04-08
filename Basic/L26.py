"""Write a program that asks the user to enter some text and then counts how many articles are
in the text. Articles are the words 'a','an', and 'the'
."""
txt =input("Enter some text: ")
articles =['a','an','the']
L= txt.split()
num =[words for words in L if words in articles]
print(num)
print(len(num))