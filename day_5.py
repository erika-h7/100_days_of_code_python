# BEGINNER PYTHON LOOPS

# For Loop
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# Average Height
# Instructions >>>>
# You are going to write a program that calculates the average student height from a list of heights.
# e.g student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g :
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 / 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164
# Example Input: 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
# Example Output: 171 (857 / 5 = 171.4)

student_heights = input("Input a list of student heights ").split()

# for loop to convert the string list in to an integer list
for n in range(0, len(student_heights)):
    # looping through the list and creating an integer in every loop
    student_heights[n] = int(student_heights[n])

# Use a for loop to find out the length
# average_height = sum(student_heights) / len(student_heights)
count_of_the_heights = 0
for student in student_heights:
    # print(f"Index: {count}, Character: {n}")
    count_of_the_heights += 1

# print(count_of_the_heights)

# User a for loop to sum the heights
sum_of_heights = 0
for height in student_heights:
    sum_of_heights = sum_of_heights + height
    # or sum_of_heights += n

# print(sum_of_heights)

average_height = sum_of_heights / count_of_the_heights
average_height_result = round(average_height)

# print(len(student_heights))
# print(sum(student_heights))
print(f"The average height is: {average_height_result}")

# *****************************
# Instructions >>>>
# You are going to write a program that calculates the highest score from a list of scores.
# e.g student_scores = [78, 65, 89, 86, 55, 91, 64, 89]     78 65 89 86 55 91 64 89
# IMPORTANT: You are not allowed to use the max or min functions. The output words must match the example
# "The highest score in the class is: X"

student_scores = input("Input a list of student scores ➡️").split()

# This for loop iterates through the list changing the string to an integer on every iteration
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# print(student_scores)

# This loop calculates the highest number on a list
highest_number = 0
for score in student_scores:
    if score > highest_number:
        highest_number = score
print(f"✨ The highest score in the class is: {highest_number}")

# ************************************
# For loop with Range
# for number in range(1, 10, 3):
#     print(number)

# Sum all the numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)

# ************************************
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 1 and 100
# IMPORTANT: There should only be 1 print statement in your console output. It should just print the final total and
# not every step of the calculation
total_sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        total_sum += number
print(f"Final total: {total_sum}")

# OR OPTION 2
sum_total = 0
for number in range(2, 101, 2):
    sum_total += number
print(f"Final total: {sum_total}")

# ************************************
# The FizzBuzz Interview Question
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# - Your program should print each number from 1 to 100 in turn.
# - When the number is divisible by 3 then instead of printing the number it should print "Fizz"
# - When the number is divisible by 5, then instead of printing the number it should print "Buzz"
# - And if the number is divisible by both 3 and 5 e.g 15 then instead of the number it should print "FizzBuzz"
# Hint: 1.- Remember your answer should start from 1 and go up to and including 100.
#       2.- Each number/text should be printed on a separate line.
for n in range(1, 101):

    if n % 3 == 0 and n % 5 == 0:
        print("Fizz Buzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# ***********************************************
# PROJECT OF THE DAY
# Create a Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input(f"How many symbols would you like? \n"))
nr_numbers = int(input(f"How many numbers would you like? \n"))

# EASY LEVEL
# password1 = ""
# for char in range(1, nr_letters + 1):
#     password1 += random.choice(letters)
#
# for char in range(1, nr_symbols + 1):
#     password1 += random.choice(symbols)
#
# for char in range(1, nr_numbers + 1):
#     password1 += random.choice(numbers)
# print(password1)

# HARD LEVEL (my approach)
# combine the letters:
# chosen_letters = []
# for letter in range(1, nr_letters + 1):
#     chosen_letters.append(random.choice(letters))
# #print(chosen_letters)
#
# # combine the symbols:
# chosen_symbols = []
# for symbol in range(1, nr_symbols + 1):
#     chosen_symbols.append(random.choice(symbols))
# #print(chosen_symbols)
#
# # combine the numbers:
# chosen_numbers = []
# for number in range(1, nr_numbers + 1):
#     chosen_numbers.append(random.choice(numbers))
# #print(chosen_numbers)
#
# combined_data = chosen_numbers + chosen_symbols + chosen_letters
# random.shuffle(combined_data)
#
# password = ""
# for item in combined_data:
#     password += item


# HARD LEVEL (best approach)
password = []
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

random.shuffle(password)

# converting list in to a string
password_result = ""
for item in password:
    password_result += item
    
print(f"Your password is: {password_result}")