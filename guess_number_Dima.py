import random
hidden = random.randint (1,10)
guess_attempts = 1
while guess_attempts <=6:
    user_guess = int(input("guess a number from 1 to 10: "))
    if user_guess == hidden:
        print(f"your guess was correct, it was {hidden}")
        break
    guess_attempts += 1
else:
    print(f"you've failed to guess the number. it was {hidden}")