"""Create a monthly cohort-style summary: for every customer’s first purchase month,
show how many of those customers made at least one purchase in the following months.
(Use order_date and customer_id)"""
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv"

import pandas as pd
df=pd.read_csv(file_path)
# every customer’s first purchase month count cust with atleast 1 order_id
df['order_date']=pd.to_datetime(df['order_date'])
df['month']=df['order_date'].dt.to_period('M')
# print(df['month'])
df['first_month']=df.groupby("customer_id")["month"].transform('min')
print(df[["customer_id", "month", "first_month"]])
