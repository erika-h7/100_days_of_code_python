# Data types: String, Integer, Float, Boolean

#>>>>>> Concatonating a string with an interger will produce an erro
# Therefor we need to convert first the integer in to a string then concatonate
# Example:
#num_char = len(input("What is your name? \n"))
# Converting to string:
#new_num_char = str(num_char)
# Print
#print("Your name has " + new_num_char + " characters.")


###### >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Write a program that adds the digits in a 2 digit number. e.g if the input was
# 35, then the output should be 3 + 5 = 8
# HINT: 1- Try to find out the data type of two_digit_number
#       2- Think about what you learnt about subscripting
#       3- Think about type conversion

# OPTION 1
#two_digit_num = input("Write a two digit number>>>>>> \n")
# Check data type
#print(type(two_digit_num))
# Convert data type
#new_two_digit_num = int(two_digit_num)
#print(type(new_two_digit_num))
# Function that iterates with a loop and sums the digit as it's looping
def getSum(new_two_digit_num):

    sum = 0
    for digit in new_two_digit_num:
        sum += int(digit)
    return sum

#print(getSum(two_digit_num))

# OPTION 2 "BETTER"
#first_digit = two_digit_num[0]
#second_digit = two_digit_num[1]

#result = int(first_digit) + int(second_digit)
#print(str(first_digit) + " + " + str(second_digit) + " = " + str(result))



###### >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>  Write a BMI Calculator
#height = input("➡️ Enter your height in Meters👇: \n")
#weight = input("➡️ Enter your weight in Kilograms👇: \n")
#weight_int = int(weight)
#height_int = float(height)
#height_squared = height_int * height_int
#result = weight_int / height_squared
#result_bmi = int(result)
#print("****************************************************")
#print("Your Body Mass Index (BMI) is 👉 " + str(result_bmi))
#print("****************************************************")

#>>>>>>> OPTION 2 """BETTER"""
#bmi = int(weight) / float(height) ** 2
#bmi_result = int(bmi)
#print("****************************************************")
#print("Your Body Mass Index (BMI) is 👉 " + str(bmi_result))
#print("****************************************************")


###### >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>  Number Manipulation
#print(round(8/3)) # rounds the number
#print(8/3) # divides the number
#print(round(8/3, 2)) # rounds the number within 2 decimal numbers
#print(8 // 3) # chops in to one whole number and makes a float in to an integer
# f-String helps concatonate an converting data types, example:
score = 0
height = 1.56
isWinning = True
#print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")


#>>>>>>>>>>>>>>> CODING CHALLENGE
# CREATE A PROGRAM USING MATHS AND F-STRINGS THAT TELLS US HOW MANY DAYS, WEEKS, MONTHS WE HAVE LEFT IF WE LIVE UNTIL 90 YEARS OLD
# It will take your current age as an input and output a message with our time left in this format:
# You have x days, y weeks, and z months left
# HINT: There are 365 days in a year, 52 weeks in a year and 12 months in a year.
age = input("➡️ What is your current age? 👉 ")
life_lived = input("Till what age you want to live? 👉")
my_life = int(life_lived) - int(age)
days = my_life * 365
weeks = my_life * 52
months = my_life * 12
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(f"You have {days} days, {weeks} weeks and {months} months left")

#>>>>>>>>>>>>>>> TIP CALCULATOR
#
print("🤓 Welcome to the tip calculator! 👇")
bill = input("➡️ What was the total bill? 👉 $ ")
percentage = input("➡️ What percentage tip would you like to give? 10, 12 or 15 percent? 👉 % ")
percentage_tip = int(percentage)

def percentage_tiping(percentage_tip):

    if (percentage_tip == 10):
        bill_with_percentage = float(bill) * 0.10
        return bill_with_percentage

    elif (percentage_tip == 12):
        bill_with_percentage = float(bill) * 0.12
        return bill_with_percentage

    elif (percentage_tip == 15):
        bill_with_percentage = float(bill) * 0.15

        return bill_with_percentage

    else:
        print("🛑 Please enter a valid percentage tip 😅")

tip = percentage_tiping(percentage_tip)

#if tip == True:
people_to_split = input("➡️ How many people to split the bill? 👉")
people_to_split_bill = int(people_to_split)
bill_and_tip = tip + float(bill)
final_bill = bill_and_tip / people_to_split_bill
our_bill = round(final_bill, 2)

print(f"Each person should pay: ${our_bill}")

#else:
    #print("enter what I said ")

