"""1. Load iris.csv into a NumPy structured array (or record array).
Extract only the numeric columns into a pure 2D float64 array.
Compute the column-wise mean and standard deviation,
then create a new array that is the original numeric data standardized (z-score) using broadcasting."""


import numpy as np
import pandas as pd
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/iris.csv"
df=pd.read_csv(file_path)
data=np.array(df)
numeric_cols=data[:,(0,1,2,3)].astype(dtype=float)
print(numeric_cols)
col_wise_mean=np.mean(numeric_cols,axis=0)
col_wise_std=np.std(numeric_cols,axis=0)
standardized =(numeric_cols-col_wise_mean)/col_wise_std
print(standardized)