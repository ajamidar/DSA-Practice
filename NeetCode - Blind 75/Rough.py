#Calculation function.
def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator"

#Setting up permission loop.
calcPerm = True
while calcPerm:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")
    result = calculate(num1, num2, operator)
    print("Result:", result)
    askCont = input("Do you want to continue? (yes/no): ")
    if askCont.lower() != "yes": calcPerm = False