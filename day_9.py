# Beginner Dictionaries
# Grading Program

# Instructions >>>>
# You have access to a data base of student_scores in the format of a dictionary.
# The Keys in student_scores are the name of the students and the values are the exam scores.
# Write a program that converts their scores in to grades. By the end of your program, you should have a new dictionary
# called student_grades that should contain student names for keys and grades for values. The final version of the
# student grades dictionary will be checked.

# DO NOT! modify the existing student_scores dictionary.
# DO NOT! write any print statements.
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# TODO 1- Create a empty dictionary called student_grades
student_grades = {}

# TODO 2- Add the grades to student_grades
for key in student_scores:
    score = student_scores[key]
    if score >= 91:
        student_grades[key] = "Outstanding!"

    elif score >= 81:
        student_grades[key] = "Exceeds Expectations"

    elif score >= 71:
        student_grades[key] = "Acceptable"

    else:
        student_grades[key] = "Failed"

# print(student_grades)

#######################################################
# NESTING
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},
    "Mexico": {"beautiful_cities": ["Guadalajara", "Los Mochis", "Culiacan", "Chihuahua"]},
    "Germany": {"capitals": ["Berlin", "Hamburg", "Stuttgart"]},
}

# Nesting a Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities": ["Paris", "Lille", "Dijon"],
        "visits": 12,
    },
    {
        "country": "Germany",
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
        "visits": 5,
    },
]


#######################################################
# Dictionary in List Exercise

# Instructions >>>>>
# You are going to write a program that adds to a travel_log
def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg", "Novosibirsk"])
# print(travel_log)

########################################################
# The Secret Auction Program

from replit import clear
# Hint: You can call clear() to clear the output in the console.abs

from logos.logobid import logo_bid

print(logo_bid)
print("Welcome! 👋 to the Silent Auction Bid")

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:  # looping through a dictionary only gives the key (not the whole element)
        bid_amount = bidding_record[bidder]  # this gives us the value of the key we are looping through
        if bid_amount > highest_bid:  # checks if value is higher than the highest_bid
            highest_bid = bid_amount  # reassigns highest_bid to the new highest_bid
            winner = bidder  # this gives the key name to the winner variable with the highest bidding
    print(f"The winner 🏆 is {winner} with a bid of 💵 ${highest_bid}")


while not bidding_finished:  # says while this is still false
    name = input("Please write your name: 👉 ").capitalize()
    price = int(input("What's your bid? 👉 $"))
    bids[name] = price  # adds a element to the dictionary
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. 👉 ")
    if should_continue == "no":
        bidding_finished = True  # this ends the while loop
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()