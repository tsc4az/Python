print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print ("You are tall enough")
else:
    print ("Shorty!!!!!")
    print ( 6 % 2)
print ( 6 % 5)
print ( 6 % 4)
print ( 10 % 3)
number = (int(input("Give me a number and I'll tell you if it is odd or even\n")))
if number % 2 == 0 :
    print ("Even")
else:
    print ('Odd')
    print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    age = int(input("What is you age\n"))
    print("You can ride the rollercoaster")
    if age >= 18:
       print ("The cost is $12")
    else:
        print ("The cost is $7")
else:
    print("Sorry you have to grow taller before you can ride.")
    print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    age = int(input("What is you age\n"))
    print("You can ride the rollercoaster")
    if age <= 12:
       print ("The cost is $5")
    elif age < 18:
        print  ("Then cost is $7")
    else:
        print ("The cost is $12")
else:
    print("Sorry you have to grow taller before you can ride.")

print("Welcome to the rollercoaster!")
bill = 0
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is you age\n"))

    if age <= 12:
        bill = 5
        print (f"Child tickets are  ${bill}")
    elif age < 18:
        bill = 7
        print  (f"Youth tickets are ${bill}")
    else:
        bill = 12
        print (f"Adult tickets are ${bill}")
    photo = input("would you like a photo (Y or N)\n")
    if photo == "Y" or photo == "y":
        bill += 3 # add 3 to the bill

    print (f"Your total bill is ${bill}.")

else:
    print("Sorry you have to grow taller before you can ride.")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L:\n ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n ")
extra_cheese = input("Do you want extra cheese? Y or N:\n ")
bill = 0

if extra_cheese == "Y" or extra_cheese == "y":
    bill += 1

if size == "S" or size == "s":
    bill += 15
elif size == "M" or size == "m":
    bill += 20
elif size == "L" or size == "l":
    bill += 20
else:
    print ("Your choice was not correct")

if pepperoni == "Y" or pepperoni == "y":
    if size =="S" or size == "s":
        bill += 2
    else:
        bill += 3


print(f"Your final bill is: ${bill}")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print ("You ride for free")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" or wants_photo == "y":
     bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

    print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you to go?")
L_R = input("Type 'left' or 'right'\n")

if L_R == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    W_S = input("Type 'wait to wait for the boat. Type 'swim to swim across\n")
    if W_S == "wait":
        print ("You arrived at the island unharmed. There is a house with 3 doors.")
        door = input("one red, one yellow and one blue. Which colour do you choose?\n")
        if door == "red":
            print ("Burned by fire. Game Over!")
        elif door == "blue":
            print("Eaten by beasts. Game Over!")
        elif door == "yellow":
            print ("You Win!!!!!!")
        else:
            print ("Game Over!!!!!")
    else:
        print("Attacked by trout. Game Over")

else:
    print ("Fall into a hole Game over!")