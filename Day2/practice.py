#Variables & Data Types 
name = "Pratiksha"
age = 22
marks = [85, 90, 78]

print("Name:", name)
print("Age:", age)
print("Marks:", marks)

# Conditional Statements 
number = 54
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#  Loops 
n=int(input("enter number for multiplication"))
print("\nMultiplication Table of:",n)
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Functions 
def greet(user):
    return f"Hello, {user}! Welcome to Python practice."

print(greet(name))

# Factorial using loop
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print("\nFactorial of 5:", factorial(5))

#Lists & Dictionaries
fruits = ["apple", "banana", "cherry"]
print("\nList of Fruits:")
for fruit in fruits:
    print(f"I like {fruit}")

student = {"name": "Pratiksha", "age": 22, "grade": "A"}
print("\nStudent Details:")
for key, value in student.items():
    print(f"{key}: {value}")

# String Manipulation 
text = "Python Programming"
print("\nString Operations:")
print(text.lower())
print(text.upper())
print(text.replace("Python", "Advanced Python"))

#  Nested Loops
print("\nPattern Printing:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Function with Parameters & Return 
def average(a, b, c):
    return (a + b + c) / 3

print("\nAverage of 3 numbers:", average(10, 20, 30))

