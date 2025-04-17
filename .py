

### **1. Calculator**
#A simple calculator that performs basic arithmetic operations.

def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Choose an operation: +, -, *, /")
    operation = input("Enter operation: ")

    if operation == '+':
        print(f"Result: {num1 + num2}")
    elif operation == '-':
        print(f"Result: {num1 - num2}")
    elif operation == '*':
        print(f"Result: {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid operation!")

calculator()