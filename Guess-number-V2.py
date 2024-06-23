import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Prompt the user to guess the number
while True:
    try:
        guess = int(input("Guess the number (between 1 and 10): "))
        
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
            continue
        
        # Check if the guess is correct
        if guess == number:
            print(f"Congratulations! You guessed the correct number: {number}")
            break
        elif guess < number:
            print("Too low! Try guessing higher.")
        else:
            print("Too high! Try guessing lower.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

