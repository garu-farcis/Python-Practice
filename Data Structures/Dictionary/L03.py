"""For this problem, use the dictionary from the beginning of this chapter whose keys are month
names and whose values are the number of days in the corresponding months.
(a) Ask the user to enter a month name and use the dictionary to tell them how many days
are in the month.
(b) Print out all of the keys in alphabetical order.
(c) Print out all of the months with 31 days.
(d) Print out the (key-value) pairs sorted by the number of days in each month
(e)Modify the program from part (a) and the dictionary so that the user does not have to
know how to spell the month name exactly. That is, all they have to do is spell the first
three letters of the month name correctly.

Given a list of strings words = ["hello", "world", "python", "is", "awesome"], use a single list comprehension to create a
new list containing only words with length > 4, converted to uppercase"""
words = ["hello", "world", "python", "is", "awesome"]
my_list=[i.upper() for i in words if len(i)>4]
print(my_list)

month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months = {m: d for m, d in zip(month_names, days)}

print(months)
user_input = input("Please enter a month name: ").capitalize()
print(months[user_input])
sort_dict ={k:v for k,v in sorted(months.items(), key= lambda x:x[0])}
print(sort_dict)
print(sorted(months.keys()))
sort_days ={k:v for k,v in months.items() if months[k]==31}
print(sort_days)
sort_bydays ={v:k for k,v in sorted(months.items(), key= lambda x:x[1])}
print(sort_bydays)
user_in =input('enter first 3 letters of the month ').capitalize()
match = [k for k in months if k[:3].lower() == user_in]
val =match[0]
print('the month and days are', months[val])
