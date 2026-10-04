# Python Type Casting
# Type casting means converting one data type into another.


# String to Integer
age = "21"

print(age)
print(type(age))

age = int(age)

print(age)
print(type(age))


# String to Float
number = "10.5"

number = float(number)

print(number)
print(type(number))


# Integer to Float
num = 10

result = float(num)

print(result)
print(type(result))


# Float to Integer
price = 99.99

result = int(price)

print(result)
print(type(result))


# Integer to String
number = 100

result = str(number)

print(result)
print(type(result))


# Boolean conversion
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))


# List to Tuple
numbers = [1, 2, 3, 4]

result = tuple(numbers)

print(result)
print(type(result))


# Tuple to List
numbers = (1, 2, 3, 4)

result = list(numbers)

print(result)
print(type(result))


# Set conversion
numbers = [1, 2, 2, 3, 3, 4]

result = set(numbers)

print(result)
print(type(result))