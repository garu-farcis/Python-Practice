"""Calculate a 3-order rolling average of revenue for each customer (sorted by order_date).
Include only customers who have at least 4 orders and show the original revenue alongside"""

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv"

import pandas as pd
pd.set_option('display.max_columns', None)

df=pd.read_csv(file_path)
df['revenue']=df['quantity'] * df['unit_price']
df = df.sort_values(["customer_id", "order_date"])

result = df[
    df.groupby("customer_id")["customer_id"].transform("size") >= 4
].copy()

result["rolling_avg_3"] = (
    result.groupby("customer_id")["revenue"]
    .rolling(3)
    .mean()
    .reset_index(level=0, drop=True)
)

print(f'my results are {result}')