"""Clean and Normalize Sensor Data
Given a NumPy array of shape (n_rows, n_features) with possible NaN values:

Remove rows that contain any NaN
Normalize each column to have mean = 0 and std = 1
Return the cleaned and normalized array. Do it efficiently (avoid loops)."""
