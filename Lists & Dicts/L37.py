def longestPalindrome( s: str) -> str:
    my_string = list(s)
    bits = []
    for i in range(0, len(my_string)):
        bits.append(my_string[i:i+3])
    palin=[each for each in bits if each==each[::-1] and len(each)>2 ]
    print(palin)

word=longestPalindrome('babad')
print(word)


s='PAYPALISHIRING'