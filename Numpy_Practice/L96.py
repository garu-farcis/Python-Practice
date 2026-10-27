"""From the Titanic data, build a nested dictionary of the form:
   {pclass: {sex: {'count': int, 'survival_rate': float}}}
   Use only Python data structures + NumPy for the calculations (no pandas groupby)."""

import numpy as np
import pandas as pd
fil_p="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/titanic.csv"
df=pd.read_csv(fil_p)
unique_classes=df['Pclass'].unique()
data=np.array(df)
print(data)