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

#guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback!='c':
        if low!= high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback=input(f" is {guess} too high (H), too low (L), or correct (C)".lower())
        if feedback == 'h':
           high = guess - 1
        elif feedback == 'l':
           low = guess + 1
    print(f"your number is {guess}")

computer_guess(220)

