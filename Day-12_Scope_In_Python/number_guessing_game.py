# Just like I did in js link: https://github.com/akashmore1/Javascript-Concepts-Everything/tree/main/Guess%20the%20Number%20Game

import random


def playGame():
    number = random.randint(1, 101)
    print('Welcome to number guessing game\n')
    print('I am thinking about a number between 1 to 100')
    difficulty = input('Choose a dificulty: (easy or hard): ')
    if difficulty == 'easy':
        attempts_remaining = 10
    elif difficulty == 'hard':
        attempts_remaining = 6
    while (attempts_remaining > 0):
        print(f'You have {attempts_remaining} attempts remaining')
        guessed_number = int(input('Guess number: '))
        if guessed_number > number:
            print('Too high')
        elif guessed_number < number:
            print('Too low')
        else:
            print(f"Guessed correct number, it's {number}")
            return
        attempts_remaining -= 1

    print(f'Failed better luck next time. The number was {number}')


playGame()
