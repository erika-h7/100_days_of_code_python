# HIGHER VS LOWER GAME


from vs_game.game_data import data
from vs_game.art import *
import random
from replit import clear


def play_game():
    print(logo)
    score = 0
    is_game_over = False
    # random_a = data[random.randint(0, 49)]
    # random_b = data[random.randint(0, 49)]
    random_a = random.choice(data)
    random_b = random.choice(data)


    # TODO: Create a while loop inside the function, if the user gets the correct answer the game keeps going, at same
    #  time storing previous data to keep comparing
    while not is_game_over:

        while random_a == random_b:
            random_b = data[random.randint(0, 49)]

        while random_b == random_a:
            random_a = data[random.randint(0, 49)]

        print(f"Compare A: {random_a['name']}, a {random_a['description']}, from {random_a['country']}")
        print(random_a['follower_count'])

        print(vs)
        print(f"Against B: {random_b['name']}, a {random_b['description']}, from {random_b['country']}")
        print(random_b['follower_count'])

        answer = input("Who has more followers? Type 'A' or 'B': ").upper()

        if random_a['follower_count'] > random_b['follower_count'] and answer == 'A':
            score += 1
            random_b = random_a
            print(f"Correct, You're score is ✨: {score}")
            print("------------------------------------")
            clear()

        elif random_b['follower_count'] > random_a['follower_count'] and answer == 'B':
            score += 1
            random_a = random_b
            print(f"Correct, You're score is ✨: {score}")
            print("------------------------------------")
            clear()

        else:
            is_game_over = True
            print(f"Sorry that's wrong 😔. Final score: {score}")


play_game()
