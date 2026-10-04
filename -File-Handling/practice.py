with open("student.txt", "w") as file:
    file.write("Name: Kartheek\n")
    file.write("Course: CSE\n")
    file.write("College: Sri Indu College\n")


with open("student.txt", "r") as file:
    print(file.read())


with open("student.txt", "a") as file:
    file.write("Skill: Python\n")


with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())


with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(str(i) + "\n")


with open("numbers.txt", "r") as file:
    numbers = file.readlines()

print(numbers)


with open("names.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Kiran\n")
    file.write("Arun\n")


with open("names.txt", "r") as file:
    names = file.readlines()

for name in names:
    print(name.strip())