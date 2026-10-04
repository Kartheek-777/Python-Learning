import pandas as pd
import numpy as np


data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya", "Arjun", "Sneha"],
    "Age": [21, 22, 20, 23, 21, 22],
    "Department": ["CSE", "ECE", "CSE", "AIML", "CSE", "AIML"],
    "Marks": [85, 72, 91, 88, 65, 95],
    "City": ["Hyderabad", "Khammam", "Warangal", "Hyderabad", "Vijayawada", "Hyderabad"]
}

df = pd.DataFrame(data)

print(df)


# Basic information

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())


# Selecting columns

print(df["Name"])
print(df[["Name", "Marks"]])


# Filtering

print(df[df["Marks"] > 80])

print(df[df["Age"] >= 22])

print(df[df["Department"] == "CSE"])

print(df[(df["Marks"] > 80) & (df["Age"] >= 21)])


# Sorting

print(df.sort_values("Marks"))

print(df.sort_values("Marks", ascending=False))


# Adding a column

df["Passed"] = df["Marks"] >= 40

print(df)


# Updating values

df.loc[df["Marks"] > 90, "Grade"] = "A+"
df.loc[(df["Marks"] >= 80) & (df["Marks"] <= 90), "Grade"] = "A"
df.loc[df["Marks"] < 80, "Grade"] = "B"

print(df)


# Statistics

print(df["Marks"].mean())
print(df["Marks"].median())
print(df["Marks"].max())
print(df["Marks"].min())
print(df["Marks"].sum())


# Grouping

print(df.groupby("Department")["Marks"].mean())

print(df.groupby("City")["Marks"].mean())


# Counting values

print(df["Department"].value_counts())

print(df["City"].value_counts())


# Missing values

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [80, np.nan, 90, np.nan]
}

new_df = pd.DataFrame(data)

print(new_df.isnull())
print(new_df.isnull().sum())

new_df["Marks"] = new_df["Marks"].fillna(new_df["Marks"].mean())

print(new_df)


# Removing duplicates

data = {
    "Name": ["A", "B", "A", "C"],
    "Marks": [80, 90, 80, 70]
}

new_df = pd.DataFrame(data)

print(new_df)

new_df = new_df.drop_duplicates()

print(new_df)


# CSV

# df = pd.read_csv("students.csv")
# df.to_csv("students_output.csv", index=False)