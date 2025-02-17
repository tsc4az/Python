print(len("Hello"))
print("Hello"[0])
print("Hello"[4])
print("Hello"[-1])
 # len(12345)
len("Hello")
print(type("Hello"))
print(type(123))
print(type(3.1456))
print(type(True))
# print("Number of letters in your name: " + len(input("Enter your name")))
# answer
print("Number of letters in your name: " + str(len(input("Enter your name\n"))))
print("My age: " + str(12))
print(123 + 456)
print(7-3)
print(3*2)
print(6/3) #float
print(5//3) #int -- rounds
print(2**2) #2^2 (2 to the power of 2
print(2**3)
#pemdas = Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
print(3 * 3 + 3 / 3 - 3) # ((3*3 = 9) + (3/3 = 1)) = 10 - 3 = 7
print(3 * 3 + 3 / 3 - 3) #Change the code so it outputs 3?
print(3 * (3 + 3) / 3 - 3)
bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))
print (round(bmi))
print(round(bmi,2))
score = 0
#user score a point
score +=1 #add 1
score -=1 #sumtract one form score
score *=1 #mutiply by one
score /=1# divided by one
print(score)
age = 12
print(f"I'm {age} years old!")
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n $"))
tip = int(input("What percentage tip would you like to give? 10 12 15\n "))
people = int(input("How many people to split the bill?\n "))
##
print(type(bill))
print(type(tip))
print(type(people))
tip_amount = ((bill * (tip/100)) / people)
print(round(tip_amount,2))
print(f"Each person pay(s) ${round((bill/people) +tip_amount,2)}")