import math
number = 25

print(math.sqrt(number))


import random
number = random.randint(1, 100)

print(number)


numbers = [10, 20, 30, 40, 50]
print(random.choice(numbers))


from math import factorial
print(factorial(6))


import datetime
print(datetime.date.today())


import math as m

print(m.pi)
print(m.pow(2, 5))


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

print(add(10, 20))
print(subtract(20, 10))