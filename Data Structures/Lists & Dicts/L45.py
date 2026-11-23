"""7. Given a list of nested lists, write a function that
returns the maximum depth of nesting.
Sample Input: [1, [2, [3, [4]]], 5]
Sample Output: 4"""

def max_depth(my_list):
    count=1
    depth_val=[]
    single_num=[]
    # max_len=len(my_list)
    max_len=0
    for each in my_list:
        if isinstance(each,list):
            count= max(count,1+max_depth(each))
        else:
            single_num.append(each)
    # print(single_num)
    # max_val=depth_val[::-1]
    return count

def max_d(my_list):
    for each in my_list:
        if isinstance(each, list):
            return 1+max_depth(each)

    return my_list


x = [1, [2, [3, [4]]], 5]

resusl = max_d(x)
print(resusl)


x=[1, [2, [3, [4]]], 5]
res=max_depth(x)
print(res)


