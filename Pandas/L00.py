import pandas as pd
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
print(df)
print(df["Name"].values)
print(df.to_csv('my_pandas_test_file',sep=','))
ages = pd.Series([22, 35, 58,43,56,432,56,43,66,765,3,22,44,222,445,231,1,122,43,5], name="Ages")
ages.to_csv("ages",sep=',',index=True)
print(ages)
print(ages.max())
print(ages.shape)
print(ages.describe())
print(df.describe())

guess=pd.read_csv("ages")
print(guess)
print(guess.head(),guess.tail())
print(guess.dtypes)
print(guess.info())
my_file=pd.read_csv("my_pandas_test_file")
age_col=my_file["Age"]
print(age_col.values)
print(age_col.dtypes)
above_35=age_col[age_col>35]
print(above_35)
print(age_col.isin([23,41]))
adult_names=my_file.loc[my_file["Age"]>25,"Name"]
print(adult_names)
print(my_file.iloc[2:8])
print(my_file.loc[2:8])
my_file.loc[2:8,3]="assign_name"
# print(my_file["assign_name"])
print(my_file.loc[:3,3])
print(my_file)
my_file["Headers"]=my_file["Age"] +20
print(my_file)
renamed_col=my_file.rename(columns={"Headers":"Spouse_Age"})
print(renamed_col["Age"].agg)