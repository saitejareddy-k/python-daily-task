a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1.Add  2.Subtract  3.Multiply  4.Divide")
ch = int(input("Enter choice: "))

if ch == 1:
    print("Result =", a + b)
elif ch == 2:
    print("Result =", a - b)
elif ch == 3:
    print("Result =", a * b)
elif ch == 4:
    if b != 0:
        print("Result =", a / b)
    else:
        print("Division by zero not possible")
else:
    print("Invalid choice")