wordlist =['abcde','b','c','d','e','f','g','h','iabcdef','j']
largest = 0

for word in wordlist:
    for c in word:
        if c not in 'abcde':
            break
    else:
        if len(word) > largest:
            largest = len(word)
            largest_word = word

print(largest_word)