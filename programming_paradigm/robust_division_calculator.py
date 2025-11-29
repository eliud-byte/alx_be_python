def safe_divide(numerator:float, denominator:float):
    try:
        if denominator == 0:
            return "Error: Cannot divide by zero."
        return numerator / denominator
        
    except TypeError:
        return "Error: Inputs must be numeric types." 