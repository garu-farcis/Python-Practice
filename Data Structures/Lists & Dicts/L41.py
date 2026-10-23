"""Given a pandas DataFrame, coerce amount to float (invalid → NaN),
 create status = "high" if amount > 100 else "normal", and drop rows where amount is null after coercion."""


import pandas as pd
import numpy as np
df=pd.read_csv("/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv")
df['amount']=df['quantity']*df['unit_price']
# print(df)
df['amount']=df['amount'].astype(dtype=float)
df['amount']=df['amount'].fillna(value=0)
df['status']=np.where(df['amount']>100,'high','low')
mask =(df['amount'].isnull())
if mask.sum()==0:
    print(df)