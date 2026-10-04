# Writing to a file

file = open("sample.txt", "w")

file.write("Hello Python\n")
file.write("Learning file handling")

file.close()


# Reading a file

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()


# Reading line by line

file = open("sample.txt", "r")

for line in file:
    print(line.strip())

file.close()


# Reading using readlines()

file = open("sample.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# Appending to a file

file = open("sample.txt", "a")

file.write("\nPython is easy to learn.")

file.close()


# Using with statement

with open("sample.txt", "r") as file:
    content = file.read()

print(content)


# Writing multiple lines

lines = [
    "Python\n",
    "SQL\n",
    "Machine Learning\n",
    "NLP\n"
]

with open("skills.txt", "w") as file:
    file.writelines(lines)


# Reading specific number of characters

with open("sample.txt", "r") as file:
    content = file.read(10)

print(content)