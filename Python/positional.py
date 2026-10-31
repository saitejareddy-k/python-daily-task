
# Python program to demonstrate positional
# and keyword arguments

# Define a function
def student(name, age, course):
    print("Student Name:", name)
    print("Student Age:", age)
    print("Student Course:", course)

# Demonstrating positional arguments
print("Using Positional Arguments:")
student("Teja", 20, "Python")

# Demonstrating keyword arguments
print("\nUsing Keyword Arguments:")
student(course="Python", name="Teja", age=20)
