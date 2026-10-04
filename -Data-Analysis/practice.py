import pandas as pd


data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya", "Arjun", "Sneha"],
    "Age": [21, 22, 20, 23, 21, 22],
    "Marks": [78, 92, 65, 88, 95, 72],
    "Department": ["CSE", "AIML", "ECE", "CSE", "AIML", "ECE"]
}

df = pd.DataFrame(data)

print(df)

print(df[df["Marks"] > 80])

print(df[df["Age"] == 21])

print(df[df["Department"] == "AIML"])


df["Result"] = df["Marks"] >= 40

print(df)


df["Marks"] = df["Marks"] + 5

print(df)


print(df.sort_values("Marks", ascending=False))

print(df["Marks"].mean())

print(df["Marks"].max())

print(df["Marks"].min())


print(df.groupby("Department")["Marks"].mean())

print(df["Department"].value_counts())


top_student = df.loc[df["Marks"].idxmax()]

print(top_student)


average = df["Marks"].mean()

print(df[df["Marks"] > average])