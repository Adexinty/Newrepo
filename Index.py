# Simple Calculator Program with Dynamic Handling of Integers and Floats

# Asking the user for inputs.
num1 = input("Enter the first number (integer or float): ")
num2 = input("Enter the second number (integer or float): ")

# Convert inputs to integers or floats dynamically
num1 = int(num1) if num1.isdigit() else float(num1)
num2 = int(num2) if num2.isdigit() else float(num2)

operation = input("Enter the operation (+, -, ×, ÷): ").strip()

# Performing the operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {int(result) if isinstance(num1, int) and isinstance(num2, int) else result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {int(result) if isinstance(num1, int) and isinstance(num2, int) else result}")
elif operation == "×":
    result = num1 * num2
    print(f"{num1} × {num2} = {int(result) if isinstance(num1, int) and isinstance(num2, int) else result}")
elif operation == "÷":
    if num2 != 0:
        result = num1 / num2
        # For division, keep it a float to ensure accuracy
        print(f"{num1} ÷ {num2} = {result}")
    else:
        print("Division by zero is not allowed!")
else:
    print("Invalid operation entered.")
