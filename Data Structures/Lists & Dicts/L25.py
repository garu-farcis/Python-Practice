"""2. You are given a dictionary mapping student names to lists of scores.
 Return a new dictionary containing only students whose average score is strictly greater than 80, with the average rounded to 1 decimal place as the value.
Sample Input: {"Alice": [85, 90, 78], "Bob": [70, 65, 80], "Charlie": [92, 88, 95]}
Sample Output: {"Alice": 84.3, "Charlie": 91.7}"""

my_dct={"Alice": [85, 90, 78], "Bob": [70, 65, 80], "Charlie": [92, 88, 95]}
new_dic = {
    name: round(sum(scores) / len(scores), 1)
    for name, scores in my_dct.items()
    if sum(scores) / len(scores) > 80
}

print(new_dic)