print("CALCULATOR FOR PERFORMING SIMPLE ARITHMETIC OPERATIONS")
print("")
num1 = float(input("Enter the First Number:"))
num2 = float(input("Enter the Second Number:"))


while True:
    print("")
    print("Operations")
    print("Enter '+' for Addition")
    print("Enter '-' for Subtraction")
    print("Enter '*' for Multiplication")
    print("Enter '/' for Division")
    print("Enter 'Exit' to exit the program")
    print("")

    operator = input("Choose the operator you want to use:")

    if operator == '+':
        print("Result:",num1+num2)

    elif operator == '-':
        print("Result:",num1-num2)

    elif operator == '*':
        print("Result:",num1*num2)

    elif operator == '/':
        print("Result:",num1/num2)

    elif operator == 'Exit':
        print("Thankyou for using the Calculator Application")
        break

    else:
        print("Invalid input")
