import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize the number of attempts and a list to store the previous guesses
attempts = 3
previous_guesses = []
print("============================================")
print("Welcome to the Amazing Number Guessing Game!")
print("============================================")
print("I'm thinking of a number between 1 and 10.")
print("You have 3 attempts to guess it correctly.")
print("==============Let's begin!================")

while attempts > 0:
    # Get user's guess
    guess = int(input("Guess the number: "))

    # Check if the guess is valid
    if guess < 1 or guess > 10:
        print("Oops! That's an invalid guess. Please enter a number between 1 and 10.")
        continue

    # Check if the guess has been made before
    if guess in previous_guesses:
        print("You've already guessed that number! Try a different one.")
        continue

    # Add the guess to the list of previous guesses
    previous_guesses.append(guess)

    if guess == secret_number:
        print("===============================================================")
        print("Congratulations! You've successfully guessed the secret number!")
        print("===============================================================")
        break
    elif guess < secret_number:
        print("--------------------")
        print("Too low. Aim higher!")
        print("--------------------")
    else:
        print("--------------------")
        print("Too high. Aim lower!")
        print("--------------------")

    attempts -= 1
    print("Attempts left:", attempts)

    # Provide a hint after the first unsuccessful attempt
    if attempts == 2:
        if secret_number % 2 == 0:
            print("--------------------------------")
            print("Hint: The secret number is even.")
            print("--------------------------------")
        else:
            print("--------------------------------")
            print("Hint: The secret number is odd.")
            print("--------------------------------")

# If the user couldn't guess the number within the given attempts
if attempts == 0:
    print("Sorry, you couldn't guess the number. The correct number was", secret_number)
