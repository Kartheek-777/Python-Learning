def greet(name):
    print("Hello", name)


greet("Kartheek")


def add(a, b):
    return a + b


print(add(10, 20))


def subtract(a, b):
    return a - b


print(subtract(20, 10))


def multiply(a, b):
    return a * b


print(multiply(10, 5))


def is_even(num):
    return num % 2 == 0


print(is_even(10))
print(is_even(7))


def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(find_largest(10, 25, 15))


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print(factorial(5))


def reverse_string(text):
    return text[::-1]


print(reverse_string("Python"))


def count_vowels(text):
    count = 0

    for char in text.lower():
        if char in "aeiou":
            count += 1

    return count


print(count_vowels("Python Programming"))


def sum_list(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(sum_list([10, 20, 30, 40]))


def find_even(numbers):
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


print(find_even([1, 2, 3, 4, 5, 6]))


def square(numbers):
    result = []

    for number in numbers:
        result.append(number * number)

    return result


print(square([1, 2, 3, 4, 5]))