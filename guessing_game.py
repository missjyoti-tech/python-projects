import random
# Computer chooses a random number between 1 and 100
secret_number = random.randint(1, 100)

# Count the number of valid attempts
attempts = 0

print(" Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")

while True:

    # Ask the user for a guess
    guess = int(input("Guess a number (1-100): "))

    # Check whether the number is within the valid range
    if guess < 1 or guess > 100:
        print(" Please enter a number between 1 and 100.")
        continue

    # Count the valid guess
    attempts += 1

    # Compare the guess with the secret number
    if guess > secret_number:
        print(" Too high! Try again.")

    elif guess < secret_number:
        print(" Too low! Try again.")

    else:
        print(" Correct!")
        print(f"You guessed the number in {attempts} attempts.")
        break


  
    
