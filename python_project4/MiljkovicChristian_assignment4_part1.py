# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #4

import random

# start while loop

while True:

# ask for size of the dice and make sure it isn't a negative number

    size_dice = int(input("How many sides on your dice (4-20)? "))

    if size_dice <= 0:
        print("That is not a valid number.")
    else:
        break
print()
print("Thanks! Here we go ...")
print()

# loop variable that breaks the while loop and also accumulator variable for both the number of rolls, doubles, and numbers for average later

a = 0

doubles=0

number_dice1=0

number_dice2=0

loop=True

# create while loop ***remember that it is random.randint

while loop:
    dice_1= random.randint(1,size_dice)
    dice_2= random.randint(1,size_dice)
    a= a + 1
    print(a,end=".")
    print(" die number 1 is",dice_1,"and die number 2 is",dice_2)

# create accumulation of numbers rolled for each dice
    number_dice1= number_dice1 + dice_1

    number_dice2= number_dice2 + dice_2
    
    
# create accumulation for doubles

    if dice_1==dice_2:
        doubles= doubles + 1
    
# create the break in the loop due to snake eyes

    if dice_1 == 1 and dice_2==1:
        loop=False
print()
print("You got snake eyes! Finally! On try number",a,end="")
print("!")

# calculate the percentage of doubles the user got and format it

percent_of_doubles= (doubles/a)*100

form_percent_of_doubles=format(percent_of_doubles,".2f")

# print doubles output

print("Along the way you rolled doubles",doubles,"times (",end="")
print(form_percent_of_doubles,end="% ")
print("of all rolls were doubles)")

# calculate the average roll for each dice

average_roll_1= (number_dice1/a)

average_roll_2= (number_dice2/a)

# format average roll

form_average_roll_1= format(average_roll_1,".2f")
form_average_roll_2= format(average_roll_2,".2f")

print("The average roll for die #1 was",form_average_roll_1)
print("The average roll for die #2 was",form_average_roll_2)


