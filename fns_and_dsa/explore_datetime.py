from datetime import datetime, timedelta

def display_current_datetime():
    """Returns the current date and time formatted as a string"""
    current_date = datetime.now()
    return current_date.strftime("%Y-%m-%d %H:%M:%S")

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    """Calculates a future date based on the number of daus provided."""
    now = datetime.now()
    future_date = now + timedelta(days=number_of_days)
    return future_date.strftime("%Y-%m-%d")

print(calculate_future_date())
