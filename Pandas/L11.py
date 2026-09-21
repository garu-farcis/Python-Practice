"""Create a summary that shows, for every region and status combination:
   - count of orders
   - total revenue
   - average discount
Then unstack the status level so Completed and Cancelled appear as separate columns."""

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv"

import pandas as pd
df=pd.read_csv(file_path)
df['revenue']=df['quantity'] * df['unit_price']
region_stus=df[df.groupby(['region','status'])].agg(
    count_order=('quantity','count'),
    total_revenue=('revenue','sum'),
    avg_discount=('discount','mean')
)
print(region_stus)
# stats=region_stus[region_stus['status'].isin(['Completed','Cancelled'])].reset_index(drop=True)