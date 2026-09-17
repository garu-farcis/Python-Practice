"""For each customer, calculate:
   - total number of orders
   - total revenue
   - average discount received
   - number of Cancelled orders
Return only customers who placed at least 3 orders, sorted by total revenue descending."""
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv"

import pandas as pd
df=pd.read_csv(file_path)
total_orders=df['quantity'].sum()
df['revenue']=df['quantity'] * df['unit_price']
customer_stats = df.groupby('customer_id').agg(
    total_orders=('order_id', 'nunique'),
    total_revenue=('revenue', 'sum'),
    average_discount=('discount', 'mean'),
    cancelled_orders=('status', lambda x: (x == 'Cancelled').sum())
)
customer_stats=customer_stats[customer_stats['total_orders']>=3]
customer_stats=customer_stats.sort_values('total_revenue',ascending=False)
print(customer_stats)



