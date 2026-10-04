import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


numbers = np.array([10, 20, 30, 40, 50])

print(numbers + 5)
print(numbers * 2)
print(np.mean(numbers))
print(np.max(numbers))
print(np.min(numbers))


numbers = np.arange(1, 21)

print(numbers)
print(numbers[numbers % 2 == 0])
print(numbers[numbers > 10])


marks = np.array([65, 78, 92, 55, 88, 70])

print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
print(np.sort(marks))


data = {
    "Name": ["Rahul", "Anu", "Kiran", "Priya", "Arjun"],
    "Age": [21, 22, 20, 23, 21],
    "Marks": [75, 92, 68, 88, 95]
}

df = pd.DataFrame(data)

print(df)
print(df["Name"])
print(df[df["Marks"] >= 80])

df["Passed"] = df["Marks"] >= 40

print(df)


df["Marks"] = df["Marks"] + 5

print(df)


print(df["Marks"].mean())
print(df["Marks"].max())
print(df["Marks"].min())


x = [1, 2, 3, 4, 5]
y = [20, 35, 30, 50, 45]

plt.plot(x, y)
plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Sales")
plt.show()


names = ["A", "B", "C", "D"]
marks = [80, 90, 70, 85]

plt.bar(names, marks)
plt.title("Marks")
plt.show()


df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 75, 90]
})

sns.scatterplot(data=df, x="Hours", y="Marks")
plt.show()