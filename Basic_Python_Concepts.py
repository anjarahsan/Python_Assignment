# Arithmetic operations in Python
# Input two numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b if b != 0 else "Cannot divide by zero"

# Display results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)