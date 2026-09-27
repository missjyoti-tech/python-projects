# Number Guessing Game

A simple Python number guessing game where the computer randomly selects a number between 1 and 100, and the user tries to guess it.

## Features

- Computer generates a random number between 1 and 100
- User can enter guesses until the correct number is found
- Gives a "Too high" or "Too low" hint after each guess
- Checks whether the guess is within the valid range
- Counts the number of valid attempts
- Displays the total attempts when the correct number is guessed

## Concepts Practiced

This project helped me practice:

- Variables
- User input
- `if-elif-else` statements
- `while` loops
- `continue` and `break`
- Comparison operators
- The `random` module
- `random.randint()`
- Type conversion using `int()`
- f-strings

## How It Works

1. The computer generates a random number between 1 and 100.
2. The user enters a guess.
3. The program checks whether the guess is between 1 and 100.
4. If the guess is too high, the program displays **"Too high!"**.
5. If the guess is too low, the program displays **"Too low!"**.
6. If the guess is correct, the game ends and displays the number of attempts.

## How to Run

Make sure Python is installed on your computer.

Open the terminal inside the project folder and run:

```bash
python number_guessing.py
