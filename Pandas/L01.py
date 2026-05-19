import pandas as pd
import numpy as np
s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s)
d = {"b": 1, "a": 0, "c": 2}
pd.Series(d)
print(d)
print(pd.Series(d, index=["b", "c", "d", "a"]))
print(pd.Series(6, index=["b", "c", "d", "a"]))
print(s.iloc[0])

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth",
            "Smith, Mrs. Anna",
            "Johnson, Mr. David",
            "Williams, Miss Emma",
            "Brown, Mr. James",
            "Davis, Mrs. Sophia",
            "Miller, Mr. Michael",
            "Wilson, Miss Olivia",
        ],
        "Age": [22, 35, 58, 28, 45, 19, 33, 41, 50, 26],
        "Sex": [
            "male",
            "male",
            "female",
            "female",
            "male",
            "female",
            "male",
            "female",
            "male",
            "female",
        ],
    }
)
df.to_csv("sample_data")
print(df.groupby('Age')['Name'].apply(list))
print(df.groupby('Sex')['Age'].mean())

d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}


df1 = pd.DataFrame(d)
print(df1)
data = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "S10")])
print(data)
iris= pd.read_csv("sample_data")
print(iris.head())
iris=iris.assign(newid_name=iris["Age"]*2)
print(iris.head())
df = pd.DataFrame(np.random.randn(10, 4), columns=["A", "B", "C", "D"])
print(df)
print(df - df.iloc[0])
print(df * 5 + 2)
df1 = pd.DataFrame({"a": [1, 0, 1], "b": [0, 1, 1]}, dtype=bool)

df2 = pd.DataFrame({"a": [0, 1, 1], "b": [1, 1, 0]}, dtype=bool)

print(df1 & df2)
print(df.transpose())
print(np.exp(df))
print(np.asarray(df))
ser = pd.Series([1, 2, 3])
idx = pd.Index([4, 5, 6])
print(np.maximum(ser, idx))
print(iris.info())
print(iris.iloc[1:4].to_string())
