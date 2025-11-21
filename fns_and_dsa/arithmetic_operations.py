def perform_operation(num1, num2, operation):
    
    try:
        match operation:
            case 'add':
                return f"{num1} + {num2} = {num1 + num2}"
            case 'subtract':
                return f"{num1} - {num2} = {num1 - num2}"
            case 'multiply':
                return f"{num1} x {num2} = {num1 * num2}"
            case 'divide':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero!")
                return f"{num1} ÷ {num2} = {num1 / num2:.2f}"

    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero!")
