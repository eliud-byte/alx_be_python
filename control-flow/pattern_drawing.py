print("Hello User!!!")
print("Enter a positive integer and I'll draw you an asterisk square!")

# Prompt user for pattern size
try:
    integer = int(input("Enter the size of the pattern: "))
    width = integer

    while integer > 0:
        for w in range(width):
            print("*", end="")
        integer -= 1
        print()
    
except ValueError:
    print("Invalid entry!")

# Draw the pattern