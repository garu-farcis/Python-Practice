"""4. Load timeseries.npy. Create a lagged version of the series (shift by 3 positions, filling the beginning with NaN).
Then compute the covariance between the original series and the lagged series (ignoring NaNs)."""
import numpy as np
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/timeseries.npy"
data=np.load(file_path)
shift_pos=3
lag_ver=np.full_like(data,fill_value=np.nan,dtype=float)
lag_ver[3:]=data[:-3]
print(lag_ver)
val= ~np.isnan(lag_ver)
covar=np.cov(data)
covar1=np.cov(val)
print(covar,covar1)