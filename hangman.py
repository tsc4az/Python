

chosen_word = random.choice(word_list)
print(chosen_word)

display =[]
for add_dash in range(0, len(chosen_word)):
    display.append("_")

C_list =[]
for cw in range(0, len(chosen_word)):
    C_list.append(chosen_word[cw])

print("".join(display))

live = 6
while C_list != display:
    guess = input("Guess a letter: ").lower()
    l = False
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess
            l = True

    if l == False:
        live -= 1

    if live == 0:
        print(stages[live])
        print("You Lose")
        break #exit the game

    print(stages[live])

    print("".join(display))
    if C_list == display:
        print("You win")

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."


    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.