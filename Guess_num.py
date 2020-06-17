import random

name = input('Hello! Whats your name? ')
guess = ''

while guess != number:
    number = random.randint(1, 12)
    guess = int(input('Guess what number I\'m thinking! '))
    if guess < number:
        print('Your too low!')
    elif guess > number:
        print('Your to high!')
    elif guess == number:
        print(f'Good job {name}! You\'ve got the right number!')
        break