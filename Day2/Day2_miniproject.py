# Mini Project: Simple Calculator

print("Simple Calculator")
print("Operations: +, -, *, /")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator: ")

if op == "+":
    print(f"Result: {a + b}")
elif op == "-":
    print(f"Result: {a - b}")
elif op == "*":
    print(f"Result: {a * b}")
elif op == "/":
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator")
