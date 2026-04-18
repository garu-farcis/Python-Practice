"""Write a program that repeatedly asks the user to enter product names and prices. Store all
of these in a dictionary whose keys are the product names and whose values are the prices.
When the user is done entering products and prices, allow them to repeatedly enter a product
name and print the corresponding price or a message if the product is not in the dictionary."""

prod_names=['ice','axe','pants']
prod_prices =[20,10,30]
my_dict = dict(zip(prod_names,prod_prices))
print(my_dict)
ques= input("enter product name ")
res ={k:v for k,v in my_dict.items() if k==ques}
print(res)