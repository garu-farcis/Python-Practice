"""Convert order_date to datetime. Resample the data by month and compute:
   - total revenue
   - number of unique customers
   - average order value
Show the result as a DataFrame with proper month-end dates."""

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv"

import pandas as pd
from datetime import datetime
df=pd.read_csv(file_path)
df['order_date']=pd.to_datetime(df['order_date'])
print(df)
df['month']=df['order_date'].dt.month
df['revenue']=df['quantity'] * df['unit_price']
df['month']=df['order_date'].dt.month
print(df['month'])
print(df)
df=df.set_index('month')
cust_stats=df.groupby('month').agg(
    total_revenue=('revenue','sum'),
    unique_cust=('customer_id','nunique'),
    avg_value = ('revenue','mean')
)
print(cust_stats)
