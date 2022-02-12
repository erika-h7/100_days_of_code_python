# Functions With Outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Name: {formated_f_name} {formated_l_name}"  # return keyword ends a function


# print(format_name("erika", "herrera"))

#################################################
# Multiple Return Values
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"  # this ends the function if this is true and escapes the rest of
        # the function block
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Name: {formated_f_name} {formated_l_name}"  # return keyword ends a function


# Instructions >>>>
# First convert this function is_leap so that instead of printing "Leap Year", or "Not Leap Year". It should return True
# if it's a leap year and return False if it's Not a Leap Year.
# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
# days_in_month(year=2022, month=2)
# And it will use this information to work out the number of days in the month, then return that as the output, e.g.
# 28
# The list month_days contains the number of days in a month from January to December for a non-leap year. A leap year
# has 29 days in February.
# Hint:

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month! please enter a valid month!"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


year = int(input("Enter a Year: "))
month = int(input("Enter a Month: "))
days = days_in_month(year, month)
print(days)

print(is_leap(2024))
