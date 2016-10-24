# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #7


# Part A

# ask user for their name and make it lower case

name=input("Name: ")

clean_name=name.lower()



# run through each character in the string in order to make that they are all alphabetical

cleaner_name=""


for char in clean_name:
    if ord(char)>=97 and ord(char)<=122:
        cleaner_name+=char
        
print("Your 'cleaned up' name is:", cleaner_name)
print("Your 'cleaned up' name reduces to:")

# run through cleaned up name and add up the values of each letter and hold accumulator for total at the end




total=0
printable=""



for char in cleaner_name:
    if ord(char)==97:
        total+=1
        printable+="1 "

    elif ord(char)==98:
        total+=2
        printable+="2 " 

    elif ord(char)==99:
        total+=3
        printable+="3 "

    elif ord(char)==100:
        total+=4
        printable+="4 " 

    elif ord(char)==101:
        total+=5
        printable+="5 "


    elif ord(char)==102:
        total+=6
        printable+="6 "

    elif ord(char)==103:
        total+=7
        printable+="7 "

    elif ord(char)==104:
        total+=8
        printable+="8 "

    elif ord(char)==105:
        total+=9
        printable+="9 "

    elif ord(char)==106:
        total+=10
        printable+="10 "

    elif ord(char)==107:
        total+=11
        printable+="11 "

    elif ord(char)==108:
        total+=12
        printable+="12 "

    elif ord(char)==109:
        total+=13
        printable+="13 "
        
    elif ord(char)==110:
        total+=14
        printable+="14 "

    elif ord(char)==111:
        total+=15
        printable+="15 "

    elif ord(char)==112:
        total+=16
        printable+="16 "


    elif ord(char)==113:
        total+=17
        printable+="17 "



    elif ord(char)==114:
        total+=18
        printable+="18 "


    elif ord(char)==115:
        total+=19
        printable+="19 "


    elif ord(char)==116:
        total+=20
        printable+="20 "



    elif ord(char)==117:
        total+=21
        printable+="21 "


    elif ord(char)==118:
        total+=22
        printable+="22 "




    elif ord(char)==119:
        total+=23
        printable+="23 "



    elif ord(char)==120:
        total+=24
        printable+="24 "



    elif ord(char)==121:
        total+=25
        printable+="25 "


    elif ord(char)==122:
        total+=26
        printable="26 "


actual_printout=printable.replace(" "," + ",len(cleaner_name)-1)

print(actual_printout,end="= ")
print(total)


#### Part B

# create accumulator in order to help with running through the total string
new_total=0
sub_total=0

# create if statement in order to take into account that the names number may not be smaller than 10

if total>9:


# create while loop so that you can reduce the number constantly

    while total>9:
        

# range goes 0,1,2,3,4 if its range(5)
        
        for i in range(len(str(total))):
            total=str(total)
            sub_total+=int(total[i])
            

        total=sub_total
        print("Further reduction:",total)


 # condition to break out of the while loop


        if total<=9:
            break
        else:
            new_total=total
            break







new_total2=0
sub_total2=0
              


if new_total>9:

    # create the second while loop so that you can reduce the number constantly

        while new_total>9:
            

    # range goes 0,1,2,3,4 if its range(5)
            
            for i in range(len(str(new_total))):
                new_total=str(new_total)
                sub_total2+=int(new_total[i])
                

            new_total=sub_total2
            print("Further reduction:",new_total)


     # condition to break out of the while loop

            
            if new_total<=9:
                new_total2=new_total
                break
else:
    new_total2=total



# create if-elif statements for the personality traits

if new_total2==0:
    print("This name means...emptiness")

elif new_total2==1:
    print("This name means...independence")

elif new_total2==2:
    print("This name means...diplomatic")

elif new_total2==3:
    print("This name means...charming")

elif new_total2==4:
    print("This name means...harmony")

elif new_total2==5:
    print("This name means...adventure")

elif new_total2==6:
    print("This name means...love")

elif new_total2==7:
    print("This name means...spirituality")

elif new_total2==8:
    print("This name means...business")

elif new_total2==9:
    print("This name means...determined")
    
   




