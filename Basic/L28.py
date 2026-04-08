"""(a) Ask the user to enter a sentence and print out the third word of the sentence.
(b) Ask the user to enter a sentence and print out every third word of the sentence."""
sent = input('Enter a sentence: ')
print(sent)
L= sent.split()
print(L[2])
sent1= input('Enter a sentence: ')
print(sent1)
L1= sent1.split()
val = [i for i in L1[2]]
print(val)
