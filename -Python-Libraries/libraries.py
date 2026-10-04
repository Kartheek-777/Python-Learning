import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# NumPy

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
print(numbers[0])
print(numbers[1:4])
print(numbers.shape)
print(numbers.dtype)

print(np.zeros(5))
print(np.ones(5))
print(np.arange(1, 11))
print(np.linspace(1, 10, 5))

print(np.sum(numbers))
print(np.mean(numbers))
print(np.max(numbers))
print(np.min(numbers))
print(np.std(numbers))

numbers = np.array([1, 2, 3, 4, 5])

print(numbers + 10)
print(numbers * 2)
print(numbers ** 2)


matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)
print(matrix.shape)
print(matrix[0])
print(matrix[:, 1])


# Pandas

data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 92, 78, 88]
}

df = pd.DataFrame(data)

print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

print(df["Name"])
print(df["Marks"])

print(df.iloc[0])
print(df.iloc[0:2])

print(df[df["Marks"] > 80])

df["Grade"] = ["B", "A", "C", "B"]
print(df)

df.loc[0, "Marks"] = 90
print(df)

df = df.sort_values("Marks")
print(df)

print(df["Marks"].mean())
print(df["Marks"].max())
print(df["Marks"].min())


# Handling missing values

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [80, np.nan, 90, 75]
}

df = pd.DataFrame(data)

print(df.isnull())
print(df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print(df)


# Reading CSV

# df = pd.read_csv("students.csv")
# print(df.head())


# Matplotlib

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Line Chart")
plt.show()


# Bar chart

names = ["A", "B", "C", "D"]
marks = [80, 90, 75, 85]

plt.bar(names, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()


# Scatter plot

plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot")
plt.show()


# Seaborn

data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [45, 50, 55, 65, 72, 85]
}

df = pd.DataFrame(data)

sns.scatterplot(data=df, x="Hours", y="Marks")
plt.title("Study Hours vs Marks")
plt.show()

sns.histplot(df["Marks"])
plt.title("Marks Distribution")
plt.show()