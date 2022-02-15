#################### SCOPE #######################

# enemies = 1
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)

# Global Scope
# player_health = 10
#
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
#
# drink_potion()

#################### GUESS A NUMBER #######################
# Imports
from replit import clear
import random

print("Welcome, to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. 🔢")

# Global variables
random_num = 0
game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


# TODO 1: Create a function called random_number with a random number from 1 to 100.
def random_number():
    random_num = random.randint(1, 100)
    return  random_num

# TODO 2: Create a variable that stores the number to be guessed
the_num = random_number()

# TODO 5: Create a make a guess function
def make_a_guess():
    make_guess = int(input("Make a guess: "))
    return make_guess

# TODO 3: Create the difficulty of the game easy, gives you 8 tries
def easy_level():
    print("You have 10 attempts remaining to guess the number")
    my_guess = make_a_guess()
    guess_count = 0
    attempt_count = 10

    while guess_count < 9:
        attempt_count = attempt_count -1

        if my_guess < the_num:
            print("Too low.")
            print("Guess again.")
            print(f"You have {attempt_count} attempts remaining to guess the number")
            my_guess = make_a_guess()
            guess_count += 1

        elif my_guess > the_num:
            print("Too high.")
            print("Guess again.")
            print(f"You have {attempt_count} attempts remaining to guess the number")
            my_guess = make_a_guess()
            guess_count += 1
            attempt_count = attempt_count -1
        elif my_guess == the_num:
            return print(f"You're guess is correct! The answer is {my_guess} ")
    return print("You ran out of attempts sorry!")

# TODO 4: Create the difficulty of the game hard, gives you 5 tries
def hard_level():
    print("You have 5 attempts remaining to guess the number")
    my_guess = make_a_guess()
    guess_count = 0
    attempt_count = 5

    while guess_count < 4:
        attempt_count = attempt_count - 1

        if my_guess < the_num:
            print("Too low.")
            print("Guess again.")
            print(f"You have {attempt_count} attempts remaining to guess the number")
            my_guess = make_a_guess()
            guess_count += 1
        elif my_guess > the_num:
            print("Too high.")
            print("Guess again.")
            print(f"You have {attempt_count} attempts remaining to guess the number")
            my_guess = make_a_guess()
            guess_count += 1
        elif my_guess == the_num:
            return print(f"You're guess is correct! The answer is {my_guess} ")

    return print("You ran out of attempts sorry!")

# TODO 6: Create play game function
def play_game():
    if game_level == 'hard':
        hard_level()
    elif game_level == 'easy':
        easy_level()
    else:
        return print("Please input the correct word")

play_game()