"""Dictionaries provide a convenient way to store structured data. Here is an example dictionary:
d=[{'name':'Todd','phone':'555-1414','email':'todd@mail.net'},
{'name':'Helga','phone':'555-1618','email':'helga@mail.net'},
{'name':'Princess','phone':'555-3141','email':''},
{'name':'LJ','phone':'555-2718','email':'lj@mail.net'}]
Write a program that reads through any dictionary like this and prints the following:
(a) All the users whose phone number ends in an 8
(b) All the users that don’t have an email address listed"""


d=[{'name':'Todd','phone':'555-1414','email':'todd@mail.net'},
{'name':'Helga','phone':'555-1618','email':'helga@mail.net'},
{'name':'Princess','phone':'555-3141','email':''},
{'name':'LJ','phone':'555-2718','email':'lj@mail.net'}]
# print(d[0])
L =[{k:v for k,v in i.items()} for i in d]
# print(L)
phone_nums=[{'phone':[i['phone'] ]} for i in d if i['phone'][-1]=='8']
print(phone_nums)
no_email=[{'name':[i['name']]} for i in d if i['email']=='']
print(no_email)



# for i in range(len(d)):
#     print(d[i])
#     for j in d[i].items():
#         print(j)
        # if re.match(r'\d*8$',j):
        #     print(j)
# L=defaultdict(list)
# for item in d:
#     if item['phone']%10==8:
#         L[item['phone']].append(item['phone'])
# print(L)