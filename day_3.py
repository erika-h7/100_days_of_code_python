# CONTROL FLOW AND LOGICAL OPERATORS

# Instructions >>>>
# 1.- Write a program that works out wether if a given number is an odd or even number
# Even numbers can be divided by 2 with no remainder.
# e.g 86 is even because 86 / 2 = 43
# 43 has no decimal places. Therefore the division is clean. 

# e.g 59 is odd because 59 / 2 = 36.875
# 36.875 is not a whole number, it has decimal places. Therefore there is a remainder of 0.875, so the division is not clean

# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
number = int(input(" ➡️  Which number do you want to check? 👉 "))

if (number % 2) == 0:
    print(f"✨✨ {number} is an even number!")
else:
    print(f"🛑 {number} is an odd number!")


# Instructions >>>>
# 1.- Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height
# 2.- It should tell them the interpretation of their BMI based on the BMI value.
# - Under 18.5 they are underweight
# - Over 18.5 but below 25 they have a normal weight
# - Over 25 but below 30 they are overweight
# - Over 30 but below 35 they are obese
# - Above 35 they are clinically obese
height = float(input("➡️ ➡️ Enter your height in m: "))
weight = float(input("➡️ ➡️ Enter your weight in kg: "))

bmi = weight / height ** 2

if bmi <= 18.5:
    print("👎 You are underweight! 😕")
elif bmi > 18.5 and bmi < 25:
    print("👍 You have normal weight! 😃")
elif bmi > 25 and bmi < 30:
    print("🛑 You are overweight!! 😲")
elif bmi > 30 and bmi < 35:
    print("🛑 You are obese!! 😧")
elif bmi > 35:
    print("🛑 You are clinically obese!!! 😵‍💫")

print(f"✨✨ Your bmi is {round(bmi)}")


# Instructions >>>> 💪 THIS IS A DIFFICULT CHALLENGE 💪
# 1.- Write a program that works out wether if a given year is a leap year.
# A normal year has 365 days, leap years have 366 days, with an extra day in February.
# The reason why we have leap years is really fascinating, this video does it more justice:
# https://www.youtube.com/watch?v=xX96xng7sAE
# Hint:
#  This is how you work out wether if a particular year is a leap year.
#   - On every year that is evenly divisible by 4
#   - Except every year that is evenly divisible by 100
#   - Unless the year is also evenly divisible by 400

year = int(input("➡️ ➡️ Which year do you want to check? 👉"))

def leap_year(year):
    if year % 4 == 0:
        pass

        if year % 100 == 0:
            pass

            if year % 400 == 0:
                #print("Unless the year is also evenly divisible by 400 (leap year)")
                print(f"✨✨✨ {year} Is a leap year!!! 🎉")
            else:
                print(f"🛑🛑 {year} Is NOTT leap year!!")
        else:
            #print("is leap but does not meet all the statements, so it's not a leap")
            print(f"✨✨✨ {year} Is a leap year!!! 🎉")
    else:
        print(f"🛑 {year} Is NOT leap year!!")

leap_year(year)
#print(f"{year} Is a leap year")


# ROLLERCOASTER TICKETS >>>>
print("👋 Welcome to the rollercoaster!")
height = int(input("📏 What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster! 🎉")
    age = int(input("🗓 What is your age? 👉"))
    if age < 12:
        bill = 5
        print("🧒 Child ticket's are $5 dlls")
    elif age <= 18:
        bill = 7
        print("🧑 Youth ticket's are $7 dlls")
    elif age >= 45 and age <=55:
        print("Everything is going to be ok. Have a free ride on us!!")
    else:
        bill = 12
        print("👩 👨 Adult ticket's are $12 dlls")
    
    wants_photo = input("📸 Do you want a photo taken? Y or N 👉")
    if wants_photo == "Y" or wants_photo == "y":
        bill += 3
    
    print(f"Your final bill is ${bill}")

else:
    print("🛑 Sorry you have to grow taller before you can ride! 😕 😔")


# INSTRUCTIONS >>>>
# Congratulations you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on user's order work out final bill.
# - Small Pizza: $15
# - Medium Pizza: $20
# - Larger Pizza: $25
# - Pepperoni for Small Pizza: +$2
# - Pepperoni for Medium or Large Pizza: +$3
# - Extra cheese for any size Pizza: +$1
print("👋👋👋 Welcome to Python Pizza🍕 Deliveries!!!")

pizza_price = 0
size = input("What size pizza do you want? S, M, L 👉")

if size == "S" or size == "s":
    pizza_price = 15
    add_peperoni = input("Do you want peperoni🍕? Y, N 👉")
    if add_peperoni == "Y" or add_peperoni == "y":
        pizza_price += 2
    
    extra_cheese = input("Do you want extra cheese🧀? Y, N 👉")
    if extra_cheese == "Y" or extra_cheese == "y":
        pizza_price += 1
        print(f"Final bill is ${pizza_price}")
    else:
        print(f"Final bill is ${pizza_price}")

elif size == "M" or size == "m":
    pizza_price = 20
    add_peperoni = input("Do you want peperoni🍕? Y, N 👉")
    if add_peperoni == "Y" or add_peperoni == "y":
        pizza_price += 3
    
    extra_cheese = input("Do you want extra cheese🧀? Y, N 👉")
    if extra_cheese == "Y" or extra_cheese == "y":
        pizza_price += 1
        print(f"Final bill is ${pizza_price}")
    else:
        print(f"Final bill is ${pizza_price}")

elif size == "L" or size == "l":
    pizza_price = 25
    add_peperoni = input("Do you want peperoni🍕? Y, N 👉")
    if add_peperoni == "Y" or add_peperoni == "y":
        pizza_price += 3
    
    extra_cheese = input("Do you want extra cheese🧀? Y, N 👉")
    if extra_cheese == "Y" or extra_cheese == "y":
        pizza_price += 1
        print(f"Final bill is ${pizza_price}")
    else:
        print(f"Final pizza price is ${pizza_price}")

# OPTION 2 >>>>
bill = 0
# pizza size
if  size == "Y" or size == "y":
    bill += 15
elif size == "M" or size == "m":
    bill += 20
else:
    bill += 25

# pizza add ons
if  add_peperoni == "Y" or add_peperoni == "y":
    if size == "S" or size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1

print(f"Final pizza bill is ${bill}")



# 💪 THIS IS A DIFFICULT CHALLENGE 💪
# Instructions >>>>
# You are going to write a program that tests the compatibility between two people.
# We're going to use the super scientific method recomended by BuzzFeed.
# To work out the love score of 2 people
# Take both peoples names and check for the number of times the letters in the word TRUES occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# - For love scores less than 10 or greater than 90, the message should be: "Your score is x, you go together like coke and mentos."
# - For love scores between 40 and 50 the message should be: "Your score is y, you are alright together".
# - Otherwise: "Your score is z"
# Hint: use the lower() and count()
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
combined_string = name1 + name2  # this concatenates the strings together in to one word

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

true = t + r + u + e
love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")



# ******************************************************************
# >>>> Treasure game
print("Welcome to Treasure Island!!")
print("Your mission is to find the treasure")

question_one = input("If you are at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()
question_two = input("You come to a lake. There is an Island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
question_three = input("You arrived at the Island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \n").lower()

if question_one == "right":
    print("You fell in to a hole. Game Over!")
else:
    question_one == "left"
    print(question_two)
    if question_two == "swim":
        print("You got attacked by a shark. Game Over!")
    else:
        question_two == "wait"
        print(question_three)
        if question_three == "red":
            print("Game Over!")
        elif question_three == "yellow":
            print("You Win!")
        else:
            question_three == "blue"
            print("Game Over!")


