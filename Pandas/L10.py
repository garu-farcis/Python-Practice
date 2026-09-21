"""Calculate a 3-order rolling average of revenue for each customer (sorted by order_date).
Include only customers who have at least 4 orders and show the original revenue alongside"""

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv"

import pandas as pd
pd.set_option('display.max_columns', None)

df=pd.read_csv(file_path)
df['revenue']=df['quantity']*df['price']
df['cust_four']=df[df['quanity']>=4]
cust_4=df.groupby('customer_id')['cust_four'].nunique()
# cust_filt=df.groupby('customer_id')
print(cust_4)