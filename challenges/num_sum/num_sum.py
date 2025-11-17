"""
This program:
    - takes a user number between 1 - 100
    - calculates the sum of all numbers from 1 up to that number.
"""

while True:
    # Catch ValueError
    try:
        # Take User input
        user_input = int(input("Enter any number between 1-100: "))
        
        # Make sure that input between 1 and 100
        if 1 <= user_input <= 100:

            # Create a list of the input
            numbers = list(range(1, user_input + 1))

            # Sum up the numbers in the list
            # Total = sum(numbers)
            total = 0
            for n in numbers:
                total += n
            print(total)
            break       
        else:
            print("Invalid number. You number must be between 1 and 100!!!")
    
    except ValueError:
        print("Invalid input. Integers only!")
