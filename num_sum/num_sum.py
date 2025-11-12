"""
This program:
    - takes a user number between 1 - 100
    - creates a list of numbers in the range 1 - 100
    - calculates the sum of all numbers in the list.
"""

while True:
    # Catch ValueError
    try:
        # Take User input
        user_input = int(input("Enter any number between 1-100: "))
        
        # Make sure that input is not more than 100 and run the program if not
        if user_input <= 100:

            # Create a range out of the input and make a list out of numbers within
            numbers = []
            for num in range(user_input):
                numbers.append(num)

            # Sum up the numbers in the list
            total = 0
            for n in numbers:
                total += n
            print(total)
            break       
        else:
            print("You number is over 100!!!")
    
    except ValueError:
        print("Invalid input. Integers only!")
