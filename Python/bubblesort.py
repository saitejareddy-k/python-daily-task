
# Python program to implement Bubble Sort

# Read the number of elements
n = int(input("Enter the number of elements: "))

# Read the list elements
arr = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

print("Original list:", arr)

# Bubble Sort algorithm
for i in range(n - 1):
    swapped = False

    for j in range(n - 1 - i):
        # Compare adjacent elements
        if arr[j] > arr[j + 1]:
            # Swap the elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    # Stop if the list is already sorted
    if not swapped:
        break

# Display the sorted list
print("Sorted list in ascending order:", arr)
uppertriangular