# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #4

while True:

# ask the user for how many columns they want

    columns= int(input("How many columns? "))

#prevent user from inputing incorrect values

    if (columns<=0):
        print("That is an invalid input, please try again.")

    else:
        break
    
# ask user for the direction they want


    
while True:

    direction= input("Direction? (l)eft or (r)ight: ")

    if direction== "l":
        break
        
    elif direction=="r":
        break

    else:
        print("That is an invlaid input, please try again.")
        


# create variable that holds the space and star character that you'll loop and accumulator variable

space=" "

star="*"

a=0

b=0

# create while loop for the first upper half of the arrow


# this is also for the right arrow

if direction=="r":

    while a!=columns:

    # print the output by multiplying the spaces by accumulator variable

       print(space*a,star)
       a+=1

    # create bottom half of the arrow and shift the row down one before starting the loop

    a=a-1

    while a>0:
        a=a-1
        print(space*a,star)


# this is for left arrow ***be careful with doing printing in while statements using < or > or = practice this for the test

elif direction=="l":

    while columns>0:

    # print the output by multiplying the spaces by accumulator variable
        columns=columns-1
        print(space*columns,star)
        
    # create second accumulator so that you can finish the bottom part of the arrow

        b+=1

    

    # create bottom half of the arrow

    # shift the bottom half up one row

    a=a+1

    while a<b:
        print(space*a,star)
        a=a+1
