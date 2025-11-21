def perform_operation(num1, num2, operation):
    # Check for addition
    if operation == 'add':
        return f"{num1} + {num2} = {num1 + num2}"
    
    # Check for subtraction
    elif operation == 'subtract':
        return f"{num1} - {num2} = {num1 - num2}"
    
    # Check for division
    elif operation == 'divide':        
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        return f"{num1} ÷ {num2} = {num1 / num2:.2f}"
    
    # Check for multiplication
    elif operation == 'multiply':
        return f"{num1} x {num2} = {num1 * num2}"

