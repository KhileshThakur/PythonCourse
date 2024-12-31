'''
Pandas : python library
-   Data manipulation
-   It provides data structure like series and Dataframe
-   handling the structured data efficiently
'''

import pandas as pd # type: ignore


#Series
data = pd.Series([10, 30, 50, 70], index=['a', 'b', 'c', 'd'])
print(data)
print(data['b'])
print(data*2)


#Dataframe
data = {
    "name": ["Alice", "Bob", "Chris", "David"],
    "age": [23, 34, 24, 54],
    "salary": [54000, 44000, 65000, 45000]
}
df = pd.DataFrame(data)
print(df)
print(df["name"])

#rows
print(df.loc[0])
print(df.iloc[1])
print(df.iloc[1:3])

#add data
df["bonus"]=df["salary"]*0.15
print(df)



#read from csv file
df=pd.read_csv("data.csv")
print(df)
df.to_csv("output.csv", index=False)
print(df.head())
print(df.tail())
print(df.info())