import random
def guessing_game():
    secret_number = random.randint
    attempts = 0
    max_attempts = 5

    print("Welcome to the Guessing Game! I'm thinking of a number between 1 and 20.")
    for attempts_taken in range(1,max_attempts + 1):
        guess = int(input(f"Attempt {attempts_taken}/ {max_attempts}: Enter your guess: "))
        if guess < secret_number:
            print("Too low! Try a higher number." )
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print("Congratulations! You guessed the correct number ({secret_number}) in ({attempts_taken}) attempts!")
            break

        attempts += 1

        if attempts == max_attempts:
            print(f"Sorry, you've used all ({max_attempts}) attempts. The secret number was ({secret_number}).")
            
guessing_game()