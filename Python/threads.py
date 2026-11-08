import threading
import time

# Function to print numbers
def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

# Function to print letters
def print_letters():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print("Letter:", ch)
        time.sleep(1)

# Creating threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Starting threads
t1.start()
t2.start()

# Waiting for threads to complete
t1.join()
t2.join()

print("Both threads completed successfully")
