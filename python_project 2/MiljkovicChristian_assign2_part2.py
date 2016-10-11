# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #2


#print the introduction
print("This program will project how much you can earn by investing money in a high-yield savings account over a 3 month period.") 


#ask the user for an initial deposit amount and interest rate
print()
initial_deposit= float(input("To begin, enter how much money you would like to initially invest: "))
interest_rate= (float(input("Next, enter your projected annual interest rate (whole number): ")))/100

#print the page break
print()
print("------- Calculating --------")
print()
 
#print and format the column headers

"""space between starting balance and interest is 4, space between interest and balance is 3"""

print("Month Starting Balance    Interest   Ending Balance")


#calculate the month starting balance, interest, and ending balance for 1st month (don't forget to divide by 12 since its monthly)

interest_1month = (initial_deposit*interest_rate)/12

balance_1month = interest_1month+initial_deposit

#calculate the month starting balance, interest, and ending balance for 2nd month

interest_2month = (balance_1month*interest_rate)/12

balance_2month = interest_2month+balance_1month

#calculate the month starting balance, interest, and ending balance for 3rd month

interest_3month = (balance_2month*interest_rate)/12

balance_3month = interest_3month + balance_2month

#format 1st row and then print

row1_initial_balance1 = format(initial_deposit,"<19,.2f")

row1_interest_1month = format(interest_1month, "<10.2f")

row1_balance_1month = format(balance_1month,"<12,.2f")

print("1    ",row1_initial_balance1, row1_interest_1month, row1_balance_1month)
                
#format 2nd row and then print

row2_initial_balance2 = format(balance_1month,"<19,.2f")

row2_interest_2month = format(interest_2month, "<10.2f")

row2_balance_2month = format(balance_2month, "<12,.2f")

print("2    ", row2_initial_balance2,row2_interest_2month, row2_balance_2month)

#format 3rd row and then print

row3_initial_balance3 = format(balance_2month,"<19,.2f")

row3_interest_3month = format(interest_3month, "<10.2f")

row3_balance_3month = format(balance_3month, "<12,.2f")

print("3    ", row3_initial_balance3,row3_interest_3month, row3_balance_3month)




"""When formatting: < means that you are putting _____ number of spaces to the right of the characters
while if you do > means you are putting _____ number of spaces to the left"""

