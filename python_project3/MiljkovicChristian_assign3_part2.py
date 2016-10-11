# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #3

# generate a random number

import random

actual_number= random.randint(1,10)

# print the intro and ask for input from the user

print("I'm thinking of a number between 1 and 10! You have 3 guesses. ")


# create the accumulator variable to record how many guesses it took and the boolean variable

a = 0
loop= True

# create the while loop that will go through the guesses and accumulate guesses

    
while loop and a < 3:

    guess= int(input("What is your guess? "))

# if the guess is correct

    if guess == actual_number:
        a = a + 1
        print("That is correct, nice job!")
        print("The secret number was",actual_number)
        print("It took you",a,"times to guess the number.")
        loop=False
        print()
# if the guess is too high

    elif guess > actual_number:
        print("Sorry that number was too high.")
        a = a + 1
        print()
# if the guess is too low

    else:
        print("Sorry that number was too low.")
        a = a + 1
        print()
# if the user runs out of guesses
       
if a == 3:
    print("You ran out of guesses.")
    print("The secret number was",actual_number)
        
