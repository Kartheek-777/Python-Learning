
# 1. Check whether a number is positive, negative or zero

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 2. Check whether a number is even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Find the largest of three numbers

a = 10
b = 25
c = 15

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# 4. Check whether a year is a leap year

year = 2024

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")


# 5. Print numbers from 1 to 20

for i in range(1, 21):
    print(i)


# 6. Print even numbers from 1 to 50

for i in range(1, 51):
    if i % 2 == 0:
        print(i)


# 7. Calculate the sum of numbers from 1 to 100

total = 0

for i in range(1, 101):
    total += i

print("Sum:", total)


# 8. Print multiplication table

number = 7

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 9. Find factorial

number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial:", factorial)


# 10. Reverse a number

number = 12345
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reverse:", reverse)


# 11. Count digits in a number

number = 123456
count = 0

while number > 0:
    number //= 10
    count += 1

print("Number of digits:", count)


# 12. Print numbers but skip 5

for i in range(1, 11):
    if i == 5:
        continue

    print(i)


# 13. Stop the loop when number reaches 7

for i in range(1, 11):
    if i == 7:
        break

    print(i)