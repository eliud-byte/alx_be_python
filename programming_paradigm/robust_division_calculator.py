def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            return "Error: Cannot divide by zero."
        division = (float(numerator) / float(denominator))
        return division
        
    except TypeError:
        return "Error: Inputs must be numeric types." 