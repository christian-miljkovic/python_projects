# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #2



#print out the intorduction

print("Hello! I'm here to help you calculate your tip.")


#have user input the cost of the bill

bill=float(input("How much was your bill? (enter a positive integer without $): "))


#ask the user how much tip they want to leave

user_tip = (float(input("How much tip would you like to leave? (enter a positive integer without $): ")))/100

         
#print thanks

print("Thanks!")

#calculate the tip based on the user input

suggested_tip=bill*user_tip
form_suggested_tip= format(suggested_tip,".2f")

print("You need to leave", end=" ")
print("$", form_suggested_tip, sep="", end=" ")
print("as a tip.")

#calculate the total bill with the actual tip

total_bill=bill+suggested_tip
form_total_bill= format(total_bill,".2f")

print("Your total bill will be", end=" ")
print("$",form_total_bill,sep="")





