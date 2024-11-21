#function for addition 
def add(num1, num2):
    return num1 + num2

#function for subtraction
def sub(num1, num2):
    return num1 - num2

#function for multiplication
def mul(num1, num2):
    return num1 * num2

#function for division
def div (num1, num2):
    if num2 == 0:
        return "Error! Invalid number"
    else:
        return num1 / num2
    
#defining main function for calculator to take user input and perform operations
def calculator():
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    #displaying the choices for operators
    print("\n select the operator")
    print("1. Addition (+)")
    print("2. subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter the choice (1,2,3,4): ")

    #performing calculation based on user choice
    if choice == '1':
        result = add (num1, num2)

    elif choice == '2':
        result = sub (num1, num2)

    elif choice == '3':
        result = mul(num1, num2)
    
    elif choice == '4':
        result = div(num1, num2)

    else:
        result= "Invalid choice"
    
    print(f" \n Result of choice {choice} is : {result}")
#running the calculator
calculator()