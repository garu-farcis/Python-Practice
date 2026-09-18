"""Find the customers who bought both “Laptop” and “Phone” (in any orders).
Return their customer_id, customer_name, and the total revenue they generated across all their orders."""
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv"

import pandas as pd
pd.set_option('display.max_columns', None)

df=pd.read_csv(file_path)
filter=df['product'].isin(['Laptop','Phone'])
my_df=df[filter]
my_df['revenue']=my_df['quantity'] * my_df['unit_price']
# print(my_df)

cust_both=my_df.groupby('customer_id')['product'].nunique()
cust_both=cust_both[cust_both==2].index
cust_stats=my_df[my_df['customer_id'].isin(cust_both)].groupby('customer_id').agg(
    cust_name=('customer_name','first'),
    total_revenue=('revenue','sum')
).reset_index()
print(cust_stats)