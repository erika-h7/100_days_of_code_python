# Beginner Function Parameters and Caesar Cipher
# Instructions >>>>
# You are painting a wall. The instructions on the paint can say the 1 can of paint can cover
# 5 squares meters of wall. Given a random height and with of wall, calculate how many cans
# of paint you'll need to buy.
# number of cans =(wall height * wall width) / coverage per can
# e.g Height = 2, Width = 4, Coverage = 5
# number of cans = (2*4) / 5 = 1.6
# But because you cant buy 0.6 of a can paint, the result should be rounded up to 2 cans.
import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


# Function
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You need {num_of_cans} cans of paint.")


paint_calc(height=test_h, width=test_w, cover=coverage)

# Prime Number Checker (Is a number that can only be cleanly divided by itself and 1).
# A prime number is greater than 1 that has no divisors other than itself and 1.
# Instructions >>>>
# You need to write a function that checks whether if the number passed into is a prime number or not.
# e.g is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# e.g number = 7
# 7/2 , 7/3, 7/4, 7/5, 7/6
n = int(input("Check this number: "))


def prime_checker(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(f"{number} it's not! a prime number")
                break
        else:
            print(f"{number} is a prime number")
    else:
        print(f"{number} is a prime number")


prime_checker(n)