"""Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters. You must solve it in O(n) time.
Sample Input: s = "eceba", k = 2
Sample Output: 3   ("ece")"""

s = "eceba"
k = 2
myls=list(s)
print(myls)
print(len(s))
als=[]
for i in range(len(myls)-k+1):
    als.append(myls[i:i+k])
max_el=[]


print(max_el)
# . Given a string s containing only lowercase letters,
# return the minimum number of characters that need to be deleted so that the frequency of every remaining character is unique.
# Sample Input: s = "aabbcc"
# Sample Output: 3   (delete one a, one b, one c → frequencies become 1,1,1 which are not unique; better delete all of one letter)
s = "aabbcc"
ls=list(s)
unique=[]
for each in ls:
    if each not in unique:
        unique.append(each)

print(f"all character is unique {''.join(map(str, unique))}")