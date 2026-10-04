# List Comprehension

numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]

print(squares)

# List comprehension with condition

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)


# Dictionary Comprehension

numbers = [1, 2, 3, 4, 5]
squares = {x: x * x for x in numbers}

print(squares)


# Set Comprehension

numbers = [1, 2, 2, 3, 4, 4]
result = {x * 2 for x in numbers}

print(result)


# Generator

def numbers():
    for i in range(1, 6):
        yield i


for number in numbers():
    print(number)


# Generator expression

squares = (x * x for x in range(1, 6))

for square in squares:
    print(square)


# Iterator

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# *args

def add(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(add(10, 20))
print(add(10, 20, 30, 40))


# **kwargs

def details(**data):
    for key, value in data.items():
        print(key, value)


details(
    name="Kartheek",
    age=21,
    course="CSE"
)


# Decorator

def decorator(function):

    def wrapper():
        print("Before function")
        function()
        print("After function")

    return wrapper


@decorator
def greet():
    print("Hello Python")

greet()


# Decorator with arguments

def check_age(function):

    def wrapper(age):
        if age >= 18:
            return function(age)
        else:
            print("Not eligible")
    return wrapper


@check_age
def vote(age):
    print("Eligible to vote")


vote(21)
vote(16)


# Lambda

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))

print(squares)


# Filter

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)


# Zip

names = ["Rahul", "Kiran", "Arun"]
marks = [80, 90, 85]

students = zip(names, marks)

for name, mark in students:
    print(name, mark)


# Enumerate

skills = ["Python", "SQL", "ML"]

for index, skill in enumerate(skills):
    print(index, skill)


# Context Manager

with open("sample.txt", "w") as file:
    file.write("Python")


# Walrus operator

if (number := 10) > 5:
    print(number)