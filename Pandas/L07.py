"""Using groupby + transform, create a column `revenue_rank_in_region` that
ranks each order’s revenue within its region (1 = highest).
Then extract the top 2 highest-revenue orders from each region."""

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv"

import pandas as pd
df=pd.read_csv(file_path)
df['revenue']=df['quantity'] * df['unit_price']
df['revenue_rank_in_region']=df.groupby('region')['revenue'].transform(lambda x:x.rank(method='min',ascending=False))
print(df)
top_2 = df[df['revenue_rank_in_region'] <= 2]
