
# Program to demonstrate except block

try:
    # Reading two numbers from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Performing division
    result = num1 / num2

    print("Division result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter only integer values.")

except Exception as e:
    print("An unexpected error occurred:", e)

print("Program execution completed.")
