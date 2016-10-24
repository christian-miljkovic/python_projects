# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #4


# create while loop in order to make sure that the number is valid

while True:

# ask the user for the amount of sticks they want to play with *** dont forget double


    number_sticks= int(input("How many sticks do you want to play with (10-100)? "))

    if (number_sticks<=0):
        print("Sorry, that is not a valid number")

    elif (number_sticks>100):
        print("Sorry, that is not a valid number")

    else:
        break
print("Great Let's play...")
print()

# create accumulator in order to determine how many sticks are left and loop variable

player1_sticks= 0

player2_sticks= 0

sticks_left=number_sticks-(player1_sticks+player2_sticks)

loop=True

# also create variables in order to keep track of players

player1=0

player2=0




# create while loop for the actual game

while loop:

# break the while loop once you get to zero sticks

    if sticks_left==0:
        break
    

# create player 1's turn

    while True:
        
        print("Turn: Player 1")
        
# if there is one stick left vs more sticks
        if sticks_left==1:
            print("There is",sticks_left,"stick on the table")
        else:
            print("There are",sticks_left, "sticks on the table.")
            
        sticks_taken1=int(input("How many sticks do you want to take (1,2 or 3)? "))
        print()


        
# prevent user from inputing invalid numbers
        if sticks_taken1>3 or sticks_taken1<=0:
            print("Sorry, that is not a valid number")
            print()
            continue
        
        elif sticks_left==2 and sticks_taken1==3:
            print("Sorry, you cannot take that many sticks")
            print()
            continue

        elif sticks_left==1 and sticks_taken1>1:
            print("Sorry, you cannot take that many sticks")
            print()
            continue
            
    
        else:
            player1_sticks= sticks_taken1 + player1_sticks

# create stick left variable in order to keep track for the end 

        sticks_left=number_sticks-(player1_sticks+player2_sticks)
        
        player1= 1 + player1

        break

    

# break the while loop once you get to zero sticks

    if sticks_left==0:
        break


# create player 2's turn

    while True:
        print("Turn: Player 2")

# if there is one stick left vs more sticks

        if sticks_left==1:
            print("There is",sticks_left,"stick on the table")
        else:
            print("There are",sticks_left, "sticks on the table.")
            
        sticks_taken2=int(input("How many sticks do you want to take (1,2 or 3)? "))
        print()
        
# prevent user from inputing invalid numbers
        if sticks_taken2>3 or sticks_taken2<=0:
            print("Sorry, that is not a valid number")
            print()
            continue

        elif sticks_left==2 and sticks_taken2==3:
            print("Sorry, you cannot take that many sticks")
            print()
            continue

        elif sticks_left==1 and sticks_taken2>1:
            print("Sorry, you cannot take that many sticks")
            print()
            continue
    
        else:
            player2_sticks= sticks_taken2 + player2_sticks
                
        
        sticks_left=number_sticks-(player1_sticks+player2_sticks)
        player2 = 1 + player2
        break

    
# whichever player has the highest amount of turns means that they were the last person to pick up the stick
print("There are no sticks left on the table! Game over.")

if player1>player2:
    print("Player 2 wins!")
      
elif player1==player2:
    print("Player 1 wins!")
    


