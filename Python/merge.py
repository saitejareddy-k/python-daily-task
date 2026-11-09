# Python program to merge two dictionaries

# Creating the first dictionary
dict1 = {
    'Name': 'Teja',
    'Age': 21,
    'Branch': 'CSE'
}

# Creating the second dictionary
dict2 = {
    'College': 'JNTUH',
    'Year': 'Final Year',
    'City': 'Hyderabad'
}

# Displaying the first dictionary
print("First Dictionary:")
print(dict1)

# Displaying the second dictionary
print("\nSecond Dictionary:")
print(dict2)

# Merging two dictionaries
merged_dict = dict1.copy()
merged_dict.update(dict2)

# Displaying the merged dictionary
print("\nMerged Dictionary:")
print(merged_dict)
