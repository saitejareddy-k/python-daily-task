# Python program to demonstrate multithreading

import threading
import time

# First thread function
def print_numbers():
    for i in range(1, 6):
        print("Number:", i)
        time.sleep(1)

# Second thread function
def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print("Letter:", letter)
        time.sleep(1)

# Main function
if __name__ == "__main__":

    # Creating two threads
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)

    # Starting threads
    t1.start()
    t2.start()

    # Waiting for both threads to complete
    t1.join()
    t2.join()

    print("Both threads have completed execution.")
