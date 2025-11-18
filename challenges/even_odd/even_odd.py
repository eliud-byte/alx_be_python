"""
This program checks whether a number is even or odd
"""

def even_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

even_odd(11)