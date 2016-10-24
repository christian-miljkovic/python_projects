# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #6


import myfunctions

import random

# create a while loop for data validation and ask user for number of questions

while True:
    
    questions=int(input("How many problems would you like to attempt? "))

    if questions>0:
        break
    else:
        print("Invalid number")
        continue

while True:

    width=int(input("How wide do you want your digits to be? 5-10: "))

    if width<=20 and width>=5:
        break
    else:
        print("Invalid width")
        continue

print("Here we go!")

# create a function that asks the user questions and records how many they got correct



def questionnaire(questions,width):

# create a loop that runs through the amount of questions desired
    
    # accumulator for answers correct

    correct=0
    
    for i in range(questions):
        print("What is ....")
        print()

# set variable equal to a random set of numbers

        n=random.randint(1,9)
        sign=random.randint(1,4)
        m=random.randint(1,9)
        
# if-elif statements that tell us which number to print

        if n==1:
            myfunctions.number_1(width)
            number1=1
        elif n==2:
            myfunctions.number_2(width)
            number1=2
        elif n==3:
            myfunctions.number_3(width)
            number1=3
        elif n==4:
            myfunctions.number_4(width)
            number1=4
        elif n==5:
            myfunctions.number_5(width)
            number1=5
        elif n==6:
            myfunctions.number_6(width)
            number1=6
        elif n==7:
            myfunctions.number_7(width)
            number1=7
        elif n==8:
            myfunctions.number_8(width)
            number1=8
        elif n==9:
            myfunctions.number_9(width)
            number1=9
        print()
        print()
# if-else statement that tells us which operator

        if sign==1:
            myfunctions.plus(width)
            operator="+"
        elif sign==2:
            myfunctions.subtract(width)
            operator="-"
        elif sign==3:
            myfunctions.division(width)
            operator="/"
        elif sign==4:
            myfunctions.multiplication(width)
            operator="*"
        
        print()
# if-elif statements that tell us the second number
        print()
        
        if m==1:
            myfunctions.number_1(width)
            number2=1
        elif m==2:
            myfunctions.number_2(width)
            number2=2
        elif m==3:
            myfunctions.number_3(width)
            number2=3
        elif m==4:
            myfunctions.number_4(width)
            number2=4
        elif m==5:
            myfunctions.number_5(width)
            number2=5
        elif m==6:
            myfunctions.number_6(width)
            number2=6
        elif m==7:
            myfunctions.number_7(width)
            number2=7
        elif m==8:
            myfunctions.number_8(width)
            number2=8
        elif m==9:
            myfunctions.number_9(width)
            number2=9
        print()
        
        answer=float(input("= "))
        print()
        a=myfunctions.check_answer(number1,number2,answer,operator)

# determine if the user was correct or not then add to the accumulator if they are

        if a==True:
            print("Correct!")
            correct+=1

        elif a==False:
            print("Incorrect, sorry.")

        print()

    print("You got",correct,"out of",questions,"correct!")


# run the function

# division works even with numbers like 4/8 beacuse of the formatting


questionnaire(questions,width)

        
        


        

