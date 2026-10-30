
# Python program to check whether a string is a palindrome

# Read a string from the user
string = input("Enter a string: ")

# Reverse the string using slicing
reverse_string = string[::-1]

# Check whether the original and reversed strings are equal
if string == reverse_string:
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
