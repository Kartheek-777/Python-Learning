# Python Basics - Practice Problems

# --------------------------------------------------
# Problem 1: Print your details
# --------------------------------------------------

name = "Kartheek"
age = 21
course = "B.Tech CSE"

print("Name:", name)
print("Age:", age)
print("Course:", course)


# --------------------------------------------------
# Problem 2: Add two numbers
# --------------------------------------------------

a = 10
b = 20

print("Sum:", a + b)


# --------------------------------------------------
# Problem 3: Calculate the area of a rectangle
# --------------------------------------------------

length = 10
width = 5

area = length * width

print("Area of rectangle:", area)


# --------------------------------------------------
# Problem 4: Calculate the area of a circle
# --------------------------------------------------

radius = 7
pi = 3.14159

area = pi * radius * radius

print("Area of circle:", area)


# --------------------------------------------------
# Problem 5: Swap two variables
# --------------------------------------------------

a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)


# --------------------------------------------------
# Problem 6: Convert Celsius to Fahrenheit
# --------------------------------------------------

celsius = 30

fahrenheit = (celsius * 9 / 5) + 32

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)


# --------------------------------------------------
# Problem 7: Calculate simple interest
# --------------------------------------------------

principal = 10000
rate = 5
time = 2

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)


# --------------------------------------------------
# Problem 8: Calculate average of three numbers
# --------------------------------------------------

a = 10
b = 20
c = 30

average = (a + b + c) / 3

print("Average:", average)


# --------------------------------------------------
# Problem 9: Extract first and last character
# --------------------------------------------------

text = "Python"

print("First character:", text[0])
print("Last character:", text[-1])


# --------------------------------------------------
# Problem 10: Reverse a string
# --------------------------------------------------

text = "Python"

reverse_text = text[::-1]

print("Original:", text)
print("Reverse:", reverse_text)


# --------------------------------------------------
# Problem 11: Count characters in a string
# --------------------------------------------------

text = "Python Programming"

print("Number of characters:", len(text))


# --------------------------------------------------
# Problem 12: Convert string to integer
# --------------------------------------------------

number = "100"

number = int(number)

print(number)
print(type(number))


# --------------------------------------------------
# Problem 13: Calculate total marks and percentage
# --------------------------------------------------

python = 85
maths = 90
science = 80

total = python + maths + science
percentage = total / 3

print("Total Marks:", total)
print("Percentage:", percentage)


# --------------------------------------------------
# Problem 14: Check whether a word exists
# --------------------------------------------------

sentence = "I am learning Python"

print("Python" in sentence)


# --------------------------------------------------
# Problem 15: Format a student message
# --------------------------------------------------

name = "Kartheek"
course = "Artificial Intelligence and Machine Learning"
college = "Sri Indu College of Engineering and Technology"

print(
    f"My name is {name}. "
    f"I am studying {course} at {college}."
)