# Program to demonstrate raise keyword

age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("You are not eligible to vote")

else:
    print("You are eligible to vote")
