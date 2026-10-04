numbers = [1, 2, 3, 4, 5, 6]

squares = [x * x for x in numbers]
print(squares)


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)


words = ["python", "sql", "machine", "learning"]

lengths = {word: len(word) for word in words}
print(lengths)


numbers = [1, 2, 3, 4, 5]

squares = (x * x for x in numbers)

for square in squares:
    print(square)


def add(*numbers):
    total = 0

    for number in numbers:
        total += number
    return total


print(add(10, 20, 30))
print(add(5, 10, 15, 20))


def student(**details):
    for key, value in details.items():
        print(key, value)


student(
    name="Kartheek",
    age=21,
    course="CSE"
)


numbers = [10, 15, 20, 25, 30]

result = list(filter(lambda x: x > 20, numbers))
print(result)


numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))
print(result)


names = ["Rahul", "Kiran", "Arun"]
marks = [80, 90, 85]

for name, mark in zip(names, marks):
    print(name, mark)


names = ["Python", "SQL", "ML"]

for index, name in enumerate(names):
    print(index, name)


def decorator(function):

    def wrapper():
        print("Starting")
        function()
        print("Finished")
    return wrapper


@decorator
def message():
    print("Hello")

message()


def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)