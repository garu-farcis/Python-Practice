"""Write a program that asks the user to enter a word and determines whether the word is a
palindrome or not. A palindrome is a word that reads the same backwards as forward """

str = input("enter your string")
rev_str= str[::-1]
if str == rev_str:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")