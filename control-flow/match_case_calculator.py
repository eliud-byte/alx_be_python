print("Welcome User!\n")
print("Let me help you with your calculations!\t")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /): ")

    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        case "/":
            result = num1 / num2
            print(f"The result is {result}.")

except ValueError:
    print("Invalid Input!")
except ZeroDivisionError:
    print("Cannot divide by zero.")
