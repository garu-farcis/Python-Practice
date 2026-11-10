"""
10 Intermediate NumPy Questions
Topics: Broadcasting · Aggregation · Ufuncs · Slicing · Indexing
Dataset: sensor_log.npy  (shape 1200 × 8)








7. Create a 1D array of shape (8,) containing the values [1.0, 0.5, 0.1, 2.0, 1.5, 0.8, 3.0, 0.2].
   Using broadcasting, multiply the entire sensor_log array by this weight vector.
   Afterwards, find the index of the row that has the maximum weighted sum (aggregation + indexing).

8. Using integer array indexing, select rows [50, 150, 300, 700, 1100] and columns [0, 2, 4, 6].
   On the resulting 5×4 array, apply the ufunc np.clip so that all values are forced
   into the range [10, 30]. Then compute the median of each column.

9. Compute the cumulative sum along axis=0 for the entire array (ufunc).
   Then, using slicing, extract only the cumulative sums at every 100th row
   (rows 99, 199, 299, …). Finally apply np.diff on this downsampled result.

10. Create two boolean masks:
    - mask_high_temp  = temperature > 24
    - mask_high_noise = noise_db > 50
    Combine them with logical operators (ufuncs) to get rows that satisfy
    (high_temp OR high_noise) AND (voltage > 11.5).
    Use the final mask to index the original array and return the mean of
    the current and vibration columns for those selected rows.
"""