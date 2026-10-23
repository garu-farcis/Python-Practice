"""Given a pandas DataFrame, coerce amount to float (invalid → NaN),
 create status = "high" if amount > 100 else "normal", and drop rows where amount is null after coercion."""


import pandas as pd
df=pd.read_csv("/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv")
df['amount']=df['quantity']*df['unit_price']
# print(df)
df['amount']=df['amount'].astype(type=float)
df['amount']=df['amount'].fillna(value=0)
if (df['amount']>100):
    df['status']='high'
else:
    df['status'] = 'normal'
print(df)