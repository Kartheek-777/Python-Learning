# Object Oriented Programming


# Class and Object

class Student:

    def display(self):
        print("Student details")

student1 = Student()
student1.display()


# Constructor

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Kartheek", 21)
student1.display()

# Instance variables

class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

student1 = Student("Kartheek", "CSE")
student2 = Student("Ramu", "ECE")

print(student1.name)
print(student1.course)

print(student2.name)
print(student2.course)


# Class variable

class Student:

    college = "Sri Indu College"

    def __init__(self, name):
        self.name = name


student1 = Student("Kartheek")
student2 = Student("Rahul")

print(student1.name)
print(student1.college)

print(student2.name)
print(student2.college)


# Instance method

class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calculator = Calculator()

print(calculator.add(10, 20))
print(calculator.multiply(5, 4))

# Inheritance

class Animal:

    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

dog = Dog()

dog.eat()
dog.bark()


# Multilevel inheritance

class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


class Puppy(Dog):

    def play(self):
        print("Playing")


puppy = Puppy()

puppy.eat()
puppy.bark()
puppy.play()


# Method overriding

class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()
dog.sound()


# Polymorphism

class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


# Encapsulation

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())


# Property

class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


student = Student("Kartheek")
print(student.name)

student.name = "Rahul"
print(student.name)


# Abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car started")


car = Car()
car.start()