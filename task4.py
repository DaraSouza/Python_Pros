import random

random_number = random.randint(1, 20)
guess = 0


while guess != random_number:
    guess = int(input("Guess the number (between 1, 20): "))
if guess > random_number:
    print("Too high! Please try again")
else:
    print("You guessed the right number. I'm very proud of you!")