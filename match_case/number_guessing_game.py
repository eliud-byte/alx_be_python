import random

# Initialisation
secret_number = random.randint(1, 10)
print("\nWelcome to the Number Guessing Game!")
print("\nI'm thinking of a number between 1 and 10")

def play_game(secret):
    # Initialise a couner before the loop
    guess_count = 0
    
    # Use a while loop that runs indefinitely until broken by a correct guess
    while True:
        try:
            # Get the user's guess inside the loop
            guess_input = input("\nGuess the number: ")
            guess = int(guess_input) # Raises ValueError if not a valid integer

            # Increment counter only after a successful conversion to int
            guess_count += 1

        except ValueError:
            print("That's not a valid number. Please enter an integer.")
            continue # Skip the rest of the loop and ask again

        # Use the match/case for the three possible outcomes: High, Low, or correct
        match guess:
            # Case 1: Guess is too high
            case _ if guess > secret:
                print("Oops, your guess is a bit high. Try again!")

            # Case 2: Guess is too low
            case _ if guess < secret:
                print("Nope, your guess is a bit low. Give it another shot!")

            #Case 3: Guess is correct (This is the 'else' if the above two don't match)
            case _:
                print(f"Congratulations! You guessed it! The number was {secret}.")
                print(f"You guessed the number in **{guess_count}** tries.")
                # Exit the loop since the game is won
                break

# Start the game
play_game(secret_number)