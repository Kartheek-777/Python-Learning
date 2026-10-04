numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])

numbers.append(60)
print(numbers)

numbers.remove(30)
print(numbers)


numbers = [5, 2, 8, 1, 9, 3]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)


numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])


numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total += num

print(total)


numbers = [10, 20, 30, 40, 50]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)


numbers = [10, 20, 30, 40, 50]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)


data = (10, 20, 30, 40, 50)

print(data)
print(data[1])
print(data[-1])


numbers = {10, 20, 30, 20, 10}

print(numbers)

numbers.add(40)
print(numbers)


a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


student = {
    "name": "Kartheek",
    "age": 21,
    "course": "CSE"
}

print(student["name"])

student["age"] = 22
student["city"] = "Hyderabad"

print(student)


for key, value in student.items():
    print(key, value)