
# Python program to swap two variables

# Reading two numbers from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Displaying values before swapping
print("\nBefore Swapping:")
print("First number (a) =", a)
print("Second number (b) =", b)

# Swapping using a temporary variable
temp = a
a = b
b = temp

# Displaying values after swapping
print("\nAfter Swapping:")
print("First number (a) =", a)
print("Second number (b) =", b)
