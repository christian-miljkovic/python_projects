# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #3


# create boolean variable for loop to end program

loop=True

answer="yes"

# create while loop to ask user to input month numerically

while loop:

# ask for the input of the date

    month= int(input("Enter a month (1-12): "))
    day= int(input("Enter a day: "))

# convert the numeric value of month to actual name of the month

    if month==1:
        real_month="January"

    elif month==2:
        real_month="Febuary"

    elif month==3:
        real_month="March"

    elif month==4:
        real_month="April"

    elif month==5:
        real_month="May"

    elif month==6:
        real_month="June"

    elif month==7:
        real_month="July"

    elif month==8:
        real_month="August"

    elif month==9:
        real_month="September"

    elif month==10:
        real_month="October"
        
    elif month==11:
        real_month="Novemeber"

    elif month==12:
        real_month="December"

    else:
        print("This is not a valid date.")
        answer=input("Would you like to continue?(yes/no): ")
        if answer=="yes":
            continue
        elif answer=="no":
            loop=False
        


# prevent the user from using invaid days

    if day > 31:
        print("That is not a valid date.")
        
            

    elif day<=0:
        print("That is not a valid date.")
                   
            
    elif day >30 and (month==4 or month==6 or month==9 or month==11):
        print("That is not a valid date.")
        
            
      
    elif month==2 and day> 28:
        print("That is not a valid date.")
               

    elif month>12 and day>31:
        print("That is not a valid date.")
        
        

# match dates with their respective days off

    if month<9 or day<2 :
        print(real_month,day,"is before the start of the Fall 2015 term.")

    elif month==9 and day==2:
        print(real_month,day,"is the Beginning of the Fall 2015 term.")

    elif month==12 and day>15:
        print(real_month,day,"is after the end of the Fall 2015 term.")

    elif month==9 and day==7:
        print(real_month,day,"is Labor Day. NYU is closed today!")
         
    elif month==10 and day==12:
        print(real_month,day,"is Fall Break. NYU is closed today!")

    elif month==10 and day==13:
        print(real_month,day,"is Legislative Day. Classes meet on a Monday schedule!")

    elif month==11 and 25<=day<=29:
        print(real_month,day,"is Thanksgiving. NYU is closed!")

    elif (month==9 and 2<day<7) or (month==9 and 7<day<=30) or (month==10 and 1<=day<12) or (month==10 and 13<day<=31) or (month==11 and 1<=day<25) or (month==11 and 29<day<=30) or (month==12 and 1<=day<15):
        print(real_month,day,"is not a holiday at NYU. NYU is open today")
        
    

# create the option to continue checking the schedule or end program    
    answer=input("Would you like to continue?(yes/no): ")
    if answer=="yes":
        continue
    elif answer=="no":
        loop=False

print("Thank you, and have a nice day!")

         







    
    
