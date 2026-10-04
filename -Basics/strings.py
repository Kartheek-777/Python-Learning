# Python Strings

# Creating a string
name = "Kartheek"

print(name)
print(type(name))


# Single quotes and double quotes
first_name = 'Kartheek'
last_name = "Lagisetti"

print(first_name)
print(last_name)


# String concatenation
first_name = "Kartheek"
last_name = "Lagisetti"

full_name = first_name + " " + last_name

print(full_name)


# String repetition
word = "Python "

print(word * 3)


# String indexing
text = "Python"

print(text[0])
print(text[1])
print(text[5])


# Negative indexing
print(text[-1])
print(text[-2])


# String slicing
print(text[0:3])
print(text[2:5])
print(text[:4])
print(text[2:])
print(text[:])


# String length
text = "Python"

print(len(text))


# Convert to uppercase
text = "python"

print(text.upper())


# Convert to lowercase
text = "PYTHON"

print(text.lower())


# Capitalize
text = "python programming"

print(text.capitalize())


# Title case
text = "python programming"

print(text.title())


# Remove spaces
text = "   Python   "

print(text.strip())


# Replace text
text = "I like Java"

print(text.replace("Java", "Python"))


# Find text
text = "Python Programming"

print(text.find("Python"))
print(text.find("Java"))


# Check whether text exists
text = "I am learning Python"

print("Python" in text)
print("Java" in text)


# String split
text = "Python,SQL,Machine Learning"

skills = text.split(",")

print(skills)


# Join strings
skills = ["Python", "SQL", "Machine Learning"]

result = ", ".join(skills)

print(result)


# Count occurrences
text = "Python is easy. Python is powerful."

print(text.count("Python"))


# Startswith and endswith
text = "python.py"

print(text.startswith("python"))
print(text.endswith(".py"))


# String formatting using f-string
name = "Kartheek"
age = 21

print(f"My name is {name} and I am {age} years old.")


# Escape characters
print("Hello\nPython")
print("Python\tProgramming")


# Raw string
path = r"C:\Users\Kartheek\Documents"

print(path)