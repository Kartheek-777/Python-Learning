# Exception Handling

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Please enter a valid number.")


# ZeroDivisionError

try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")


# Multiple exceptions

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# else

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", number)


# finally

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input.")
finally:
    print("Program finished.")


# Raising an exception

age = 15

try:
    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("Eligible")

except ValueError as error:
    print(error)


# Exception with file handling

try:
    with open("data.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")