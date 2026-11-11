
# Program to find the sum of first N natural numbers

# Read input from the user
n = int(input("Enter the value of N: "))

# Initialize sum to zero
total = 0

# Check whether N is valid
if n < 1:
    print("Please enter a positive natural number.")
else:
    # Calculate sum using for loop
    for i in range(1, n + 1):
        total = total + i

    # Display the result
    print("Sum of first", n, "natural numbers is:", total)
