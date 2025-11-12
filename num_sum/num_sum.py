"""
This program:
    - takes a user number between 1 - 100
    - creates a list of numbers in the range 1 - 100
    - calculates the sum of all numbers in the list.
"""
# Take User input
user_input = int(input("Enter any number between 1-100: "))

# Make a list out of the number in user input range
numbers = []
for num in range(user_input):
    numbers.append(num)

# Sum up the numbers in the list
total = 0
for n in numbers:
    total += n
print(total)
