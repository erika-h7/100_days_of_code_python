#### Write a program that prints the number of characters in a user's name.
# You might need to Google for a function that calculates the length of a string

# OPTION 1
#user_name = input("Enter your name: ")
#count = 0

#for s in user_name:
    #count = count + 1

#print("The length is: ", count)


# OPTION 2
#user_name = input("Enter your name: ")

#print("The lenght is: ", len(user_name))


# OPTION 3
#user_name = input("Enter your name: ")
#counter = 0
#for c in user_name:  #traverse the string “educative”
    #counter+=1  #increment the counter

#print("The length is: ", counter)  #outputs the length (9) of the string “educative”


# OPTION 4
#print(len("erika"))


# OPTION 5
#print(len(input("What is your name: ")))

##### Write a program that switches the values stored in variables a and b
#a = input("a: ")
#b = input("b: ")

# OPTION 1
#a, b = b, a

#print("a = " + a, "b = " + b)

# OPTION 2
#c = a
#a = b
#b = c

#print("a = " + a, "b = " + b)

#### Write a program that:
# 1.- Create a greeting for your program
print("Hello Welcome to the band name generator!")

# 2.- Ask the user for the city they grew up in
city = input("What city did you grew up in? \n")

# 3.- Ask the user for the name of the pet
pet_name = input("Write the name of a pet: \n")

# 4.- Combine the name of their city and pet and show them their band name
print("Your band name is: " + city + " " + pet_name)

# 5.- Make sure the cursor show in a new line
