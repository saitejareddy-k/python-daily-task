# Python program to demonstrate a lambda function

# Lambda function to add two numbers
add = lambda a, b: a + b

# Lambda function to subtract two numbers
subtract = lambda a, b: a - b

# Lambda function to multiply two numbers
multiply = lambda a, b: a * b

# Lambda function to find the square of a number
square = lambda x: x * x

# Lambda function to find the largest of two numbers
largest = lambda a, b: a if a > b else b

# Read input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Display results
print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Square of first number:", square(a))
print("Largest number:", largest(a, b))