print("Hello User!!!")
print("Enter a positive integer and I'll draw you an asterisk square!")

try:
    # Prompt user for pattern size
    integer = int(input("Enter the size of the pattern: ")) 
    width = integer
    
    while integer > 0:
        for w in range(width):
            print("*", end="") # Draw the pattern
        integer -= 1
        print()
    
except ValueError:
    print("Invalid entry!")
