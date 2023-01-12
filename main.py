"""
Program that reproduces the caesar cipher
It can encode a word with an amount of shift in the alphabet
and decode it with the same amount of shift in the
alphabet

For example : abcdefghijklmnopqrstuv
if we decide that the shift is 3, a will become the next 3 letters which is d, b will be e, etc.
To decode, we must use the same amount of shift and go back.
"""

# import the art module
import art

# prints the logo from the art module
print(art.logo)

print("Welcome To The Caesar Cipher ! ")

# alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']
# boolean variable for the while loop
should_continue = True

# function with inputs to encode and decode a word
# start_text : text that we want to encode or decode
# shift_amount : number of time we shift
# cipher_direction : whether we want to encode or decode


def caesar(start_text, shift_amount, cipher_direction):

    # empty string to store the word
    end_text = ""

    # if the cipher_direction is decode : we will shift back, so we multiply the shift_amount by -1
    if cipher_direction == "decode":
        shift_amount *= -1

    # for loop : we will go through all the letters in the start_text
    for char in start_text:

        # we look if the character is not a symbol before entering the block of code
        # must be letter to execute the block of code in the if statement
        if char in alphabet:
            # we look for the index of the letter
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        # if the character is a symbol, we simply add it in the end_text
        else:
            end_text += char
    # print the text
    print(f"The {cipher_direction}d text is {end_text}")

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message : ").lower()
        shift = int(input("Type the shift number : "))
        shift = shift % 26

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        result = input("Type 'yes' if you want to continue. Otherwise type 'no'. ").lower()
        if result == "no":
            should_continue = False
            print("Thank you for using this program. ")

    # if the user writes anything else than "encode" and "decode"
    else:
        print("Error : Try again with an appropriate command")