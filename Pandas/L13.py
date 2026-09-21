"""Using only Completed orders, find the top 3 products by total revenue in each region.
Return a DataFrame with columns: region, product, total_revenue, rank_in_region."""

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv"

import pandas as pd
df=pd.read_csv(file_path)
df['revenue']=df['quantity']*df['unit_price']
df=df[df['status']=='Completed']
# Total revenue for each product in each region
result = (
    df.groupby(["region", "product"], as_index=False)
      .agg(total_revenue=("revenue", "sum"))
)
# Rank products within each region
# df['rank_in_region']=df.groupby('region')['revenue'].transform(lambda x:x.rank(method='min',ascending=False))

result["rank_in_region"] = (
    result.groupby("region")["total_revenue"]
          .rank(method="min", ascending=False)
)
result=result[result['rank_in_region']<=3]
result = result.sort_values(["region", "rank_in_region"])
# print()
print(result)
# df.set_index('region')
#
# df=df.groupby('revenue')['products']
# print(df)