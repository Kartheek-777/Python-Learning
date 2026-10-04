# Python Input and Output

# Output using print()
print("Hello, Python")
print("Welcome to Python Programming")


# Printing multiple values
name = "Kartheek"
age = 21

print("Name:", name)
print("Age:", age)


# Taking input from the user
name = input("Enter your name: ")

print("Hello", name)


# Input is always received as a string
age = input("Enter your age: ")

print("Your age is:", age)
print("Data type:", type(age))


# Taking integer input
age = int(input("Enter your age: "))

print("You are", age, "years old.")


# Taking float input
percentage = float(input("Enter your percentage: "))

print("Your percentage is:", percentage)


# Using f-string
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")

# Using dot format method 
name =  input("Enter your name: ")
age = int(input("Enter your Age: "))

print("My name is {} and I am {} years old.".format(name, age))