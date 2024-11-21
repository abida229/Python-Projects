#Option 1: User Input
def calculator():
    try:
        # Taking user input for numbers and operation
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")
            return

        
        print(f"Result: {result}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")


calculator()

#Option 2: Variables
print("Predefined Input variables")

# Predefined variables
a = 10
b = 5

# Performing operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b if b != 0 else "undefined (division by zero)"

# Displaying the results
print(f"Addition: {a} + {b} = {addition}")
print(f"Subtraction: {a} - {b} = {subtraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division}")
