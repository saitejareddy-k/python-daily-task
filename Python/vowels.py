
# Python program to count vowels and consonants in a string

# Step 1: Read a string from the user
string = input("Enter a string: ")

# Step 2: Initialize the counters
vowels = 0
consonants = 0

# Step 3: Convert the string into lowercase
string = string.lower()

# Step 4: Check each character in the string
for char in string:

    # Step 5: Check whether the character is a vowel
    if char in "aeiou":
        vowels = vowels + 1

    # Step 6: Check whether the character is a consonant
    elif char >= 'a' and char <= 'z':
        consonants = consonants + 1

# Step 7: Display the results
print("Total number of vowels:", vowels)
print("Total number of consonants:", consonants)
