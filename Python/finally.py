
# Python program to demonstrate finally block

try:
    # Read two numbers from the user
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    # Perform division
    result = a / b

    print("Division result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid integer values.")

finally:
    print("Finally block is executed.")
    print("Program execution completed.")
