
# Control flow is used to control the execution of a program.
# Main concepts:
# 1. if, elif, else
# 2. Nested if
# 3. for loop
# 4. while loop
# 5. break
# 6. continue
# 7. pass

# 1. IF, ELIF AND ELSE


age = 21

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# elif
marks = 75

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")


# Checking positive, negative or zero
number = -10

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 2. NESTED IF

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("ID is required.")
else:
    print("Entry not allowed.")


# 3. FOR LOOP

# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)


# Loop through a list
skills = ["Python", "SQL", "Machine Learning"]

for skill in skills:
    print(skill)


# Loop through a string
name = "Python"

for character in name:
    print(character)


# Multiplication table
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 4. WHILE LOOP


count = 1

while count <= 5:
    print(count)
    count += 1


# Sum of numbers
number = 1
total = 0

while number <= 10:
    total += number
    number += 1

print("Sum:", total)

# 5. BREAK

# break stops the loop completely.

for i in range(1, 11):
    if i == 5:
        break

    print(i)

# 6. CONTINUE

# continue skips the current iteration.

for i in range(1, 11):
    if i == 5:
        continue

    print(i)

# 7. PASS

# pass does nothing.
# It is used as a placeholder.

age = 20

if age >= 18:
    pass


# Empty function
def future_function():
    pass


print("Control flow examples completed.")