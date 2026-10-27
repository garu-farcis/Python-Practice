"""3. Load titanic.csv. Create a boolean mask for passengers who survived and were in 1st or 2nd class. Using only NumPy operations, extract the ages of those passengers,
replace any missing ages with the median age of the masked group, and return the mean and standard deviation of the cleaned ages."""

import numpy as np
import pandas as pd
fil_p="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/titanic.csv"
df=pd.read_csv(fil_p)
data=np.array(df)
print(data)
Pclass=data[:,2]
surv=data[:,1]
mask=(surv==1)&(Pclass<=2)
new_data=data[mask]
median_group=np.median(new_data[:,5])
print(new_data)
ages=new_data[:,5]
print(ages)