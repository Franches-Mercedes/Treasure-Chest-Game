# Treasure Chest Game!
# This module opens up every class available within in the 'random' module
import random

# Counter to track the attempts the user has left
attempts_left = 10
# Accumulator to track total cash
total_cash = 0
# A list to check if an opened chest is trying to be opened again
opened_chests = []

# 15 random numbers from a range of 1 to 50 will be inputted into the list
chest = []
for number in range(1, 17):
    chest.append(random.randint(1, 50))

# random.randrange() will select a random index in the iChest array to place a -1 integer in the array
chest[random.randrange(1, 16)] = -1

# 0 index of the array will always be 0 since it won't be selected ever in the game
chest[0] = 0

# This was to check if my code works! :)
# this prints an array of each chest displaying a number
# print(iChest)

# Instructions for the game
print(' '*25,'Game has started!')
print('Enter a value from 1 to 15 to open a treasure chest for each attempt.')
print('If you open a treasure chest with a "-1" value then you lose the game and your money!')
print('If you open 10 chests without a "-1" value, you keep the money!\n')

# While loop to track the users 10 attempts to play the game
while attempts_left > 0:
    # During each attempt this will display how many attempts are left till they can win
    print(f'Attempts left: {attempts_left}')

    # Asks the user to pick a chest out of the 15 chests to choose
    treasure_Guess = int(input('Enter a chest number from 1 to 15: '))

    # if they input an integer that is not from 1 to 16 then the game will ask
    # them to pick an integer from 1 to 15
    if treasure_Guess not in range(1, 16):
        print('Please enter a treasure chest number from 1 to 15!\n')
        continue

    # Checks if the guess was already used in a list
    elif treasure_Guess in opened_chests:
        print('You have already opened this treasure chest. Open a different treasure chest!\n')
        continue

    # if the chest that the user opened contains a -1 integer then the game will end and display a message
    elif chest[treasure_Guess] == -1:
        print('Oops! You lost the game :(')
        break
    else:
        # if the user opens up a chest that doesn't have a -1 integer then they will
        # add that bonus number in the chest and add it to their total cash
        # then go onto their next attempt which decreases by 1 each attempt
        print(f'You just opened a chest with {chest[treasure_Guess]} dollars!\n')
        total_cash += chest[treasure_Guess]
        opened_chests.append(treasure_Guess)
        attempts_left -= 1

# if the user survives for 10 attempts without getting a -1 in a chest
# then they win their total cash and beat the game
if attempts_left == 0:
    print(f'You won ${total_cash} dollars!')
