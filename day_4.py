# RANDOMISATION AND PYTHON LISTS
import random

# 1 - 100
random_integer = random.randint(1, 10)
print(random_integer)

# 0.0000000 - 4.9999999999
random_float = random.random() * 5
print(random_float)

# ********************************************************************
# HEAD OR TAILS EXERCISE
# Instructions >>>>
# You are going to write a virtual coin toss program. It will randomly tell the user 'Heads' or 'Tails'
# Important >>>>
# The first letter should be capitalised and spelt exactly like in the example e.g Heads, not heads.
# There are many ways of doing this. But to practice what we learnt in the last lesson,
# you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
# e.g 1 means Heads, 0 means Tails
import random

coin_toss = random.randint(0, 1)

if coin_toss == 0:
    print("Tails")
if coin_toss == 1:
    print("Heads")

# ************************************************************************************
# Instructions >>>>
# You are going to write a program which wll select a random name from the list of names.
# The person selected will have to pay for everybody's food bill.
# Important >>>>
# You are not allowed to use the choice() function
# Hint: You might need the help of the len() function.
names_string = input("Give me a everybody's names, separated by a comma. ")
names = names_string.split(", ")
names_length = len(names)
print(names)
sorted_name = random.randint(0, names_length - 1)
winner_name = names[sorted_name]

# Option 2
winner = random.choice(names)
print(f"Congratulations {winner}, you are the selected person to 'Pay the bill' 🎉")

# ************************************************************************************
# Instructions >>>>
# You are going to write a program which will mark a spot with an X.
# The map is inside 3 rows of blank squares.
# Your program should allow you to enter the position of the treasure using a two-digit system.
# The first digit is the horizontal column number and the second digit is the vertical row number.e.g.
# Column 2, row 3 would be entered as: 23
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \n")

column = int(position[0])
row = int(position[1])

# this :
selected_row = map[row - 1]
selected_row[column - 1] = "X"

# or :
# map[row - 1][column - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

# ************************************************************************************
# ROCK PAPER SCISSORS GAME
# Instructions >>>>
# Rock wins against scissors
# Paper wins against rock
# Scissors wins against paper
import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: \n"))

computer_random = random.randint(0, 2)

game_hands = [rock, paper, scissors]

# if user_choice == 0:
#     print(rock)
#     print("Computer chose: ")
#
#     if computer_random == 0:
#         print(rock)
#         print("Play again, it's a tie!")
#
#     elif computer_random == 1:
#         print(paper)
#         print("Computer wins!")
#
#     elif computer_random == 2:
#         print(scissors)
#         print("You win!")
#
# elif user_choice == 1:
#     print(paper)
#     print("Computer chose: ")
#
#     if computer_random == 0:
#         print(rock)
#         print("You win!")
#
#     elif computer_random == 1:
#         print(paper)
#         print("Play again, it's a tie!")
#
#     elif computer_random == 2:
#         print(scissors)
#         print("Computer wins!")
#
# elif user_choice == 2:
#     print(scissors)
#     print("Computer chose: ")
#
#     if computer_random == 0:
#         print(rock)
#         print("Computer wins!")
#
#     elif computer_random == 1:
#         print(paper)
#         print("You win!")
#
#     elif computer_random == 2:
#         print(scissors)
#         print("Play again, it's a tie!")

# OPTION 2.
hand_name = ["Rock", "Paper", "Scissors"]


def choices():
    print(f"You Chose: \n {hand_name[user_choice]} {game_hands[user_choice]}")
    print(f"Computer Chose: \n {hand_name[computer_random]} {game_hands[computer_random]}")


if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")

elif user_choice == 0 and computer_random == 2:
    choices()
    print("You Win!")

elif computer_random == 0 and user_choice == 2:
    choices()
    print("You lose, Computer Wins!")

elif computer_random > user_choice:
    choices()
    print("You Lose!")

elif user_choice > computer_random:
    choices()
    print("You Win!!")

elif user_choice == computer_random:
    choices()
    print("It's a draw! Play again!")
