# Functions

def greet():
    print("Hello, Python")


greet()


# Function with parameters

def greet_user(name):
    print("Hello", name)


greet_user("Kartheek")


# Multiple parameters

def add(a, b):
    print(a + b)


add(10, 20)


# Return value

def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print(result)


# Default parameter

def greet(name="User"):
    print("Hello", name)


greet()
greet("Kartheek")


# Keyword arguments

def student(name, age, course):
    print(name)
    print(age)
    print(course)


student(
    name="Kartheek",
    age=21,
    course="CSE"
)


# *args

def add_all(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(add_all(10, 20))
print(add_all(10, 20, 30, 40))


# **kwargs

def student_details(**details):
    for key, value in details.items():
        print(key, value)


student_details(
    name="Kartheek",
    age=21,
    course="CSE"
)


# Lambda function

square = lambda x: x * x

print(square(5))


add = lambda a, b: a + b

print(add(10, 20))


# Map

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)


# Filter

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)


# Recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))


# Recursive countdown

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)


countdown(5)