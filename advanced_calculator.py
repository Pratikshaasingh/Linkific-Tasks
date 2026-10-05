import math

# Function Definitions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def square_root(a):
    if a < 0:
        return "Error! Negative number."
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Error! Negative number."
    return math.factorial(int(a))


# Main Program 
print("Calculator")
print("Choose operation:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")
print("^  Power")
print("%  Modulus")
print("sqrt  Square Root")
print("fact  Factorial")

operation = input("\nEnter operation: ")

# Handle single-input operations separately
if operation in ["sqrt", "fact"]:
    num = float(input("Enter number: "))
    if operation == "sqrt":
        result = square_root(num)
    else:
        result = factorial(num)
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    elif operation == "^":
        result = power(num1, num2)
    elif operation == "%":
        result = modulus(num1, num2)
    else:
        result = "Invalid operation!"

print(f"\nResult: {result}")
