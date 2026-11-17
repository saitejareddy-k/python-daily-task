# Program to find the largest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("First number is largest:", a)

elif b >= a and b >= c:
    print("Second number is largest:", b)

else:
    print("Third number is largest:", c)