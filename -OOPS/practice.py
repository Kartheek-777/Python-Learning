class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(self.name)
        print(self.age)
        print(self.course)


student = Student("Kartheek", 21, "CSE")

student.display()


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rectangle = Rectangle(10, 5)

print(rectangle.area())
print(rectangle.perimeter())


class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"

        return a / b


calculator = Calculator()

print(calculator.add(10, 20))
print(calculator.subtract(20, 10))
print(calculator.multiply(5, 4))
print(calculator.divide(20, 5))


class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


class Cat(Animal):

    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


account = BankAccount("Kartheek", 5000)

account.deposit(1000)
account.withdraw(2000)
account.display()