"""2. Using the same iris data, create a dictionary whose keys are the unique species names and whose values
 are 2D NumPy arrays containing only the rows belonging to that species.
 Then, for each species, compute the covariance matrix of its four features."""

import pandas as pd
import numpy as np

file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/iris.csv"

df=pd.read_csv(file_path)
unique_keys=df['species'].unique()
print(unique_keys)
data=np.array(df)
print(data)