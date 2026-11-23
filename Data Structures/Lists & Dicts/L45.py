"""7. Given a list of nested lists, write a function that
returns the maximum depth of nesting.
Sample Input: [1, [2, [3, [4]]], 5]
Sample Output: 4"""

def max_depth(my_list):
    count=0
    depth_val=[]
    single_num=[]
    # max_len=len(my_list)
    max_len=0
    for each in my_list:
        if isinstance(each,list):
            depth_val.extend(max_depth(each))
        else:
            single_num.append(each)
    # print(count)
    # max_val=depth_val[::-1]
    return single_num



x=[1, [2, [3, [4]]], 5]
res=max_depth(x)
print(res)


