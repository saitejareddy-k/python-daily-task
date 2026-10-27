# Python program to count the frequency of each character

# Read a string from the user
string = input("Enter a string: ")

# Create an empty dictionary
frequency = {}

# Count the frequency of each character
for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

# Display the character frequencies
print("Character frequencies:")

for char, count in frequency.items():
    print(char, ":", count)