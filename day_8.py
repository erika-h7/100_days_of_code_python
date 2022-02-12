# Caesar Cipher Part 1 - Encryption
alphabet_and_numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u',
                        'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                        '9', '0', ' ', '.', ',', 'a',
                        'b', 'c', 'd',
                        'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u',
                        'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                        '9', '0', ' ', '.', ',']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n")
shift = int(input("Type the shift number: \n"))


# TODO 1 - Create a function called 'encrypt' that takes the 'text' and 'shift' as input.
# TODO 2 - Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
#  and print the encrypted 'text'.
# TODO 3 - Call the encrypt function and pass in the user inputs. You should be able to test the code
#  and encrypt a message.
# TODO 4 - What if the user enters a shift number grater than the number of letters in the alphabet?
#   Try running the program and entering a shift number of 45.
#   Hint: Think about you can use the modulus (%).
# e.g plain_text = "hello" shift = 5 cipher_text = "mjqqt" print_output = "The encoded text is: "

def caesar(start_text, shift_amount, cipher_direction):
    if shift <= 63:
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for letter in start_text:
            position = alphabet_and_numbers.index(letter)
            new_position = position + shift_amount
            end_text += alphabet_and_numbers[new_position]
        print(f"The {cipher_direction}d text is: {end_text}")
    else:
        print(f"You entered a shift number of {shift}, please enter a valid shift number that"
              f" is less than 63! Thank you!")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
