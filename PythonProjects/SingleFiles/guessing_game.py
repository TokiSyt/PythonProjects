import random

secret_number = random.randint(1,9)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess a number 1 - 9: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
    elif guess_count == 3:
        print('Oopsie! Try again.')
