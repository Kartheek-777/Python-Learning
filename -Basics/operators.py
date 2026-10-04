# Python Operators

a = 10
b = 3


# 1. Arithmetic Operators

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


# 2. Comparison Operators

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# 3. Assignment Operators

x = 10

x += 5
print("x += 5:", x)

x -= 3
print("x -= 3:", x)

x *= 2
print("x *= 2:", x)

x /= 2
print("x /= 2:", x)


# 4. Logical Operators

age = 21
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)


# 5. Membership Operators

skills = ["Python", "SQL", "Machine Learning"]

print("Python" in skills)
print("Java" in skills)
print("Java" not in skills)


# 6. Identity Operators

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)
print(x is z)
print(x == z)


# 7. Bitwise Operators

a = 5
b = 3

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)
