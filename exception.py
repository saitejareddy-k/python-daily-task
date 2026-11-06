
# Python program to demonstrate raise keyword

# Read age from the user
age = int(input("Enter your age: "))

try:
    # Check age condition
    if age < 18:
        raise ValueError("You are not eligible to vote.")

    else:
        print("You are eligible to vote.")

except ValueError as e:
    print("Exception:", e)

finally:
    print("Program execution completed.")
