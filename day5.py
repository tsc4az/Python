fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print (fruit)
    print(fruit + " Pie")

print ("Hello")

sum = 0
max_score = 0
min_score = 0
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))


for score in student_scores:
    sum += score

for max_number in student_scores:
    if max_number > max_score:
        max_score = max_number

min_score = student_scores[0]
for min_number in student_scores:
      if min_number < min_score:
         min_score = min_number

print (sum)
print (max_score)
print (min_score)

ms =0

new_list = [8,65,89,86,55,91,64,89]
for max_n in new_list:
    if max_n > ms:
        ms = max_n
print(ms)

sum = 0
for number in range(1,101):
    sum += number

print(sum)

# FIZZ BUZZ
for number in range (1,101):
    if (number % 3) == 0 and  (number % 5) == 0:
        print("FizzBuzz")
    elif (number % 3) == 0:
        print("Fizz")
    elif (number % 5) == 0:
        print("Buzz")
    else:
        print(number)
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
password1 = ""
password2 =  ""

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for L in range (0, nr_letters):
    password.append(random.choice(letters))
for S in range (0, nr_symbols):
    password.append(random.choice(numbers))
for N in range(0, nr_numbers):
    password.append(random.choice(symbols))


for p1 in password:
    password1 += p1
#my random shuffle
#rp = random.(password, len(password))
#for p2 in range (0, len(rp)):
#    password2 += str(rp[p2])

random.shuffle(password)
#print(password) #shuffled password.
for p2 in password:
    password2 += p2


print (f"Your pass word is: {password1} or {password2}")


print (f"Your pass word is: {password1} or {password2}")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(password)

# Hard level
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")