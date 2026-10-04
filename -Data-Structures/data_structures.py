# Lists

numbers = [10, 20, 30, 40, 50]

print(numbers)
print(numbers[0])
print(numbers[-1])

numbers.append(60)
print(numbers)

numbers.insert(1, 15)
print(numbers)

numbers.remove(30)
print(numbers)

numbers.pop()
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(len(numbers))


# List slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])


# Tuples

data = (10, 20, 30, 40)

print(data)
print(data[0])
print(data[-1])
print(len(data))

print(data[1:3])


# Sets

numbers = {10, 20, 30, 20, 10}

print(numbers)

numbers.add(40)
print(numbers)

numbers.remove(20)
print(numbers)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


# Dictionaries

student = {
    "name": "Kartheek",
    "age": 21,
    "course": "CSE",
    "college": "Sri Indu College"
}

print(student)

print(student["name"])
print(student["age"])

student["age"] = 22
print(student)

student["city"] = "Hyderabad"
print(student)

student.pop("city")
print(student)

print(student.keys())
print(student.values())
print(student.items())


# Looping through a dictionary

for key, value in student.items():
    print(key, value)


# Nested data structures

students = [
    {"name": "Rahul", "age": 21},
    {"name": "Kiran", "age": 22},
    {"name": "Arun", "age": 20}
]

for student in students:
    print(student["name"], student["age"])