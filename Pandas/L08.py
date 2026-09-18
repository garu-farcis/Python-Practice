"""6. Create a multi-index DataFrame with region → category → product as the index and show:
   - total quantity sold
   - average unit_price
   - total revenue
Sort the multi-index and display only the Electronics category."""

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv"

import pandas as pd
df=pd.read_csv(file_path)
df['revenue']=df['quantity'] * df['unit_price']
cust_assets=df.groupby(['region','category','product']).agg(
    total_sold=('quantity','sum'),
    avg_unit=('unit_price','mean'),
    total_revenue=('revenue','sum')
)
print(cust_assets)
clean_assets=cust_assets.sort_index()
print(clean_assets)
dis=clean_assets.xs('Electronics',level='category')
print(f' the display is {dis}')