import numpy as np
import pandas as pd
from collections import namedtuple
Point = namedtuple("Point", "x y")
df=pd.DataFrame([Point(0, 0), Point(0, 3), (2, 3)] )
print(df)
print(pd.DataFrame.from_dict(dict([("A", [1, 2, 3]), ("B", [4, 5, 6])])))
print(pd.DataFrame.from_dict(
    dict([("A", [1, 2, 3]), ("B", [4, 5, 6])]),
    orient="index",
    columns=["one", "two", "three"],
)
)
data = np.zeros((2,), dtype=[("A", "i4"), ("B", "f4"), ("C", "S10")])
print(data)
print(pd.DataFrame.from_records(data, index="C"))

datafile = {
    "filename": ["filename_01", "filename_02"],
    "path": [
        "media/user_name/storage/folder_01/filename_01",
        "media/user_name/storage/folder_02/filename_02",
    ],
}


pd.set_option("display.max_colwidth", 50)

df=pd.DataFrame(datafile)
print(df)
df.columns = [x.upper() for x in df.columns]
print(df)


