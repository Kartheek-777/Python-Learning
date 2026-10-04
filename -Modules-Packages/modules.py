# Modules and Packages

# Importing a built-in module

import math

print(math.sqrt(25))
print(math.pow(2, 3))
print(math.factorial(5))
print(math.pi)


# Importing specific functions

from math import sqrt, factorial

print(sqrt(49))
print(factorial(5))


# Using an alias

import math as m

print(m.sqrt(64))
print(m.pi)


# Random module

import random

print(random.randint(1, 10))

numbers = [10, 20, 30, 40, 50]

print(random.choice(numbers))


# Date and time

import datetime

today = datetime.date.today()

print(today)


now = datetime.datetime.now()

print(now)


# Creating your own module

# Create another file named my_module.py

# my_module.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


# Then use:

import my_module

print(my_module.add(10, 20))
print(my_module.multiply(5, 4))


# Using aliases with your own module

import my_module as mm

print(mm.add(10, 20))


# Package example-----------

# Folder structure:
# mypackage/
#     __init__.py
#     calculator.py

# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Usage:

from mypackage.calculator import add

print(add(10, 20))