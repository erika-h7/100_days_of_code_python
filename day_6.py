# Hang Man Game!

# Step 1
# TODO 1 - Randomly chose a word from the word_list and assign it to a variable called chosen_word.
# TODO 2 - Ask the user to guess a letter and assign their answer to a variable called guess,
#  make guess lowercase.
# TODO 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


# Step 2
# TODO 4 - Create an empty list called display
#          For each letter in the chosen_word add "_" to "display"
#          So if the chosen_word was "apple", "display" should be:
#          ["_","_","_","_","_"] with 5 "_" representing each letter to guess.
# TODO 5 - Loop through each position in the chosen_word;
#          If the letter at the position matches 'guess' then reveal the letter in
#          the display at that position.
# TODO 6 - Print 'display' and you should see the 'guess' letter in the correct position
#          and every other letter replaced with '_'


# Step 3
# TODO 7 - Use a while loop to let the user guess again. The loop should only stop once the user has guessed
#          all the letters in the chosen_word and 'display' has no more blanks ("_").
#          Then you can tell the user they won.


# Step 4
# TODO 8 - Create a variable called 'lives' to keep track of the number of lives left. Set 'lives' to equal 6.
# TODO 9 - If 'guessed' is not a letter in the 'chosen_word', then reduce the 'lives' by 1.
#          If the 'lives' go down to 0 then the game should stop and it should print "You lose"
# TODO 10 -Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.


# The import for the random module
import random

# Hang Man ASCII Art
from hangman.hang_man_art import stages

# Word list of possible words in the game
from hangman.word_list import word_list

# Hangman Logo
from hangman.logo import logo

print(logo)

# Randomly chosen word from the list
chosen_word = random.choice(word_list)
print(chosen_word)

display = []

# This variable stops the while loop, when 'end_of_game' is equal to True
end_of_game = False

# This variable keeps track of the number of lives the user has left
lives = 6


# Displays the positions available for the letters (the blanks)
for _ in range(len(chosen_word)):
    display += "_"

while not end_of_game:

    guessed = input("🧐 Guess a letter: 👇️ \n   You guessed 👉  ").lower()

    if guessed in display:
        print(f"⛔️ ️You've already guessed: 👉  {guessed}")

    # This will swap the space for the letter, if letter in chosen_word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed:
            display[position] = letter

    # Check if letter not in chosen_word
    if guessed not in chosen_word:
        lives -= 1

        if lives >= 1:
            print(f"That's NOT! in the word\n🛑 You have ➡️  {lives}  ⬅️ lives remaining! ")

        # Check if out of lives, if so 'You lose' and exists the loop
        if lives == 0:
            print("🛑🛑 Game Over!🛑🛑\n")
            print(f"|||   😔 The word was: 👉 {chosen_word} 👈   |||")
            end_of_game = True

    # Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("✨✨ You Win! 🎉")
        print(f"Word is: ✨👉 {chosen_word} 👈✨")

    print(stages[lives])

    print(f"✏️ Word:  {display}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
