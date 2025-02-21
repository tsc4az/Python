def greet(): # pause 1 - Review
    print("Hello")
    print("World")
    print("!")

greet()

# Function ask a person name
def myFunction(input):
    print(f"Hey! {input}")

myFunction(input("What is your name?\n"))

# simple def about age
def life_in_weeks(age):
    weeks = (90 - age) * 52
    print(f"You have {weeks} weeks left.")


life_in_weeks(age= int(input("What is your age?\n")))
# stupit love score program
def calculate_love_score(name1, name2):
    check = ""
    total1 = 0
    total2 = 0
    for letter in name1:
        check += letter
    for letter in name2:
        check += letter
    check = check.lower()
    for letter in check:
        if letter == "t" or letter == "r" or letter == "u" or letter == "e":
            total1 += 1
        if letter == "l" or letter == "o" or letter == "v" or letter == "e":
            total2 += 1
    final = ((total1 * 10) + total2)
    print(f"Love score = {final}")

calculate_love_score("Kanye West", "Kim Kardashian")
# my solution to step 3
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
   encrypt_word = ""
   for letter in original_text:
        if letter == " ":
            encrypt_word += " "
        elif alphabet.index(letter) + shift_amount >= 26:
            encrypt_word += alphabet[alphabet.index(letter) + (shift_amount - 26)]
        elif alphabet.index(letter) + shift_amount <= 25:
            encrypt_word += alphabet[(alphabet.index(letter)) + shift_amount]

   print(f"Here is the encoded result: {encrypt_word}")

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(original_text = text,shift_amount= shift)
# Her solution to step 3
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


encrypt(original_text=text, shift_amount=shift)

#my code for step 4alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
#
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")



# def decrypt(original_text, shift_about):
#     encrypt_word = ""
#     for letter in original_text:
#         if letter == " ":
#             encrypt_word += " "
#
#     print(encrypt_word)



def encrypt(direction,original_text, shift_amount):
   encrypt_word = ""
   for letter in original_text:
        if letter == " ":
            encrypt_word += " "
        elif direction == "encode":
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            encrypt_word += alphabet[shifted_position]
        elif direction == "decode" :
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            encrypt_word += alphabet[shifted_position]

   print(f"Here is the encoded result: {encrypt_word}")

encrypt(direction=direction, original_text = text,shift_amount= shift)

# Her solution to step 4
# TODO-1: Import and print the logo from art.py when the program starts.


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

#final cipher
# TODO-1: Import and print the logo from art.py when the program starts.
import art
from art import logo
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?

stop =0
while stop < 1:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if go_again == "no":
        stop = 1


