# Python Data Types

# 1. String
name = "Kartheek"
print(name)
print(type(name))


# 2. Integer
age = 21
print(age)
print(type(age))


# 3. Float
percentage = 93.5
print(percentage)
print(type(percentage))


# 4. Boolean
is_student = True
print(is_student)
print(type(is_student))


# 5. List
skills = ["Python", "SQL", "Machine Learning"]
print(skills)
print(type(skills))


# 6. Tuple
coordinates = (10, 20)
print(coordinates)
print(type(coordinates))


# 7. Set
numbers = {10, 20, 30, 10}
print(numbers)
print(type(numbers))


# 8. Dictionary
student = {
    "name": "Kartheek",
    "age": 21,
    "course": "B.Tech CSE"
}

print(student)
print(type(student))


# Checking multiple data types
values = [
    "Python",
    100,
    10.5,
    True,
    [1, 2, 3],
    (1, 2),
    {1, 2, 3},
    {"name": "Kartheek"}
]

for value in values:
    print(value, "->", type(value))