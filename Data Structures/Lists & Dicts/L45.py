"""7. Given a list of nested lists, write a function that
returns the maximum depth of nesting.
Sample Input: [1, [2, [3, [4]]], 5]
Sample Output: 4"""

def max_depth(my_list):
    count=0
    depth_val=[]
    for each in my_list:
        if isinstance(each,list):
            count+=1
            depth_val.extend(max_depth(each))
            pass
        else:
            pass
    max_val=depth_val[::-1]
    return depth_val



x=[1, [2, [3, [4]]], 5]
res=max_depth(x)
print(res)


