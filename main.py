import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"guess the number between 1 and {x} "))
        if guess < random_number:
            print("too low, guess again")
        elif guess > random_number:
            print("too high, try again")
    print(f"yes, the guess number is {random_number}")

guess(20)