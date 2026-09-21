"""Merge sales_data with customers on customer_id.
Then calculate the average revenue per loyalty_tier and the percentage of total revenue contributed by each tier.
Sort the result by average revenue descending."""


file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv"
file_path1="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/customers.csv"
import pandas as pd
df=pd.read_csv(file_path)
df1=pd.read_csv(file_path1)
merged_df=df.merge(df1,on='customer_id')
print(merged_df)
merged_df['revenue']=merged_df['quantity'] * merged_df['unit_price']
cust_stats=(merged_df.groupby('loyalty_tier').agg(
    avg_revenue=('revenue','mean'),
    total_rev=('revenue','sum'),
    total_custs=('customer_id','count')
))
cust_stats["revenue_percentage"] = (cust_stats["total_rev"] / cust_stats["total_rev"].sum() * 100)

cust_stats=cust_stats.sort_values(by='avg_revenue',ascending=False)
print(cust_stats)
