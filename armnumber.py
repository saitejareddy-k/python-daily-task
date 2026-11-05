
# Python program to check Armstrong number

# Read a number from the user
num = int(input("Enter a number: "))

# Store the original number
original = num

# Count the number of digits
temp = num
digits = len(str(num))

# Initialize sum
sum = 0

# Calculate the sum of powers of digits
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10

# Check whether the number is Armstrong or not
if original == sum:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")
