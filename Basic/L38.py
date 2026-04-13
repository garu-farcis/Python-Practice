"""Here is an old puzzle question you can solve with a computer program. There is only one
five-digit number n that is such that every one of the following ten numbers shares exactly
one digit in common in the same position as n. Find n.
01265, 12171, 23257, 34548, 45970, 56236, 67324, 78084, 89872, 99414"""
from pprint import pprint
L= [ 10265, 12171, 23257, 34548, 45970, 56236, 67324, 78084, 89872, 99414]
L1= list(L)
pprint(L1)
for num in range(100000):
    candidate = str(num).zfill(5)

    ok = True

    for row in L:
        matches = 0

        for i in range(5):
            if candidate[i] == row[i]:
                matches += 1

        if matches != 1:
            ok = False
            break

    if ok:
        print(candidate)
        break