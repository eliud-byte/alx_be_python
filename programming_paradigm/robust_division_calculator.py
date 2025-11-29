def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            return "Error: Cannot divide by zero."
        return float(numerator / denominator)
        
    except TypeError:
        return "Error: Inputs must be numeric types." 