"""
- This program creates text based art using nested loops!
- Use nested while loops to print a pyramid pattern of asterisks (*)
"""

# Define the height of the pyramid
# Use nested while loops to achieve:
#   - The outer loop will control the number of rows.
#   - The inner loop will print spaces and then asterisks in each row,
#     creating a triangular shape.
# Adjust the number of spaces and asterisks printed within the inner
# loop based on the current row number to form a pyramid.

height = 5
row = 1

while row <= height:
    # Print leading spaces
    spaces = height - row
    space_count = 0
    while space_count < spaces:
        print(" ", end="")
        space_count += 1
    
    # Print asterisks
    asterisks = 2 * row - 1
    asterisk_count = 0
    while asterisk_count < asterisks:
        print("*", end="")
        asterisk_count += 1
    
    print()  # New line after each row
    row += 1
