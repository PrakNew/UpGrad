import pandas as pd

df = pd.read_csv("MegaMart_sales.csv")

# Create a numpy array for the above pandas dataframe

arr = df.to_numpy()


# Create a pandas dataframe from a numpy array

df_new = pd.DataFrame(arr)

df_new = pd.read_csv("MegaMart_newsales.csv")

df1 = pd.concat([df, df_new], ignore_index=True, sort=False)

df2 = df1.drop_duplicates()

pattern = r"^AZ-2011-\d{7}$"
invalid_order_ids = df2[~df2["Order ID"].str.match(pattern)]


df_sorted = df2.sort_values(by="Sales", ascending=False)

top_25 = df_sorted.head(25)

cat_furn = top_25[top_25["Category"] == "Furniture"]


df3 = df2[(df2["Sales"] > 250) & (df2["Profit"] > 50)].sort_values(
    by="Sales", ascending=False
)[3:4]


condition = df2["Profit"] < 1

df4 = df2[~condition]
df4["test"] = df4["Profit"] / df4["Quantity"]

df4 = df4[df4["Category"] == "Technology"].sort_values(by="Sales", ascending=True)



import numpy as np
import pandas as pd

# The file is stored at the following path:
# 'https://media-doselect.s3.amazonaws.com/generic/NMgEjwkAEGGQZBoNYGr9Ld7w0/rating.csv'
df = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/NMgEjwkAEGGQZBoNYGr9Ld7w0/rating.csv')

df["Training"] = df.Rating.apply(lambda x: "Yes" if x<3.5 else "No")
# Provide your answer below

print(df.head(5))

#  In the dataframe created above, find the department that has the most efficient team (the team with minimum percentage of employees who need training).
dep = "Sales"
n1 = df[(df["Training"]=="Yes") & (df["Department"]==dep)]["Department"].count()
n2 = df[df["Department"]==dep].Department.count()

print(n1/n2)

rating = df

for i in ['Finance', 'HR', 'Sales', 'Marketing']:
    print(i, len(rating[(rating['Training'] == 'No') & (rating['Department'] == i)]) / len(rating[rating['Department'] == i]) * 100)