
# Program to find length, smallest and largest numbers in a list

# Create an empty list
numbers = []

# Read the number of elements
n = int(input("Enter the number of elements: "))

# Check whether the list size is valid
if n <= 0:
    print("Please enter a positive number of elements.")

else:
    # Read list elements from the user
    for i in range(n):
        num = int(input("Enter element: "))
        numbers.append(num)

    # Find the length of the list
    length = len(numbers)

    # Find the smallest number
    smallest = min(numbers)

    # Find the largest number
    largest = max(numbers)

    # Display the list
    print("\nGiven List:", numbers)

    # Display the results
    print("Length of the list:", length)
    print("Smallest number in the list:", smallest)
    print("Largest number in the list:", largest)
