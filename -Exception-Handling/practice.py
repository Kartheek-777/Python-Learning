try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input.")


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


try:
    numbers = [10, 20, 30]

    index = int(input("Enter index: "))

    print(numbers[index])

except ValueError:
    print("Enter a valid index.")

except IndexError:
    print("Index does not exist.")


try:
    with open("data.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist.")


try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("You are not eligible.")

    print("Eligible")

except ValueError as error:
    print(error)


try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("Number:", num)

finally:
    print("Done.")