# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #8


mylist=[]

# create data input 

while True:
    n=int(input("Enter a positive integer greater than or equal to 10: "))
    if n>=10:
        break
    else:
        print("That is an invalid input")
        
# appending P's based upon number range

for i in range(n):
    mylist.append("P")


mylist[0]= "N"
mylist[1]= "N"

# checking first non-specical number 2 and multiples of 2

for i in range(2, len(mylist)):
    if mylist[i]=="P":

        for j in range(i*2, len(mylist), i):
            mylist[j] = "N"

# checking next number 3 and multiples of 3

for i in range(3, len(mylist)):
    if mylist[i]=="P":

        for j in range(i*3, len(mylist), i):
            mylist[j] = "N"
            
# checking next number 5 and multiples of 5

for i in range(5, len(mylist)):
    if mylist[i]=="P":

        for j in range(i*5, len(mylist), i):
            mylist[j] = "N"


# convert P's into their given number and print it out

counter=0

for i in range(len(mylist)):
    
    if mylist[i]=="P":                       
        print(i,end=' ')                        
        counter+=1
                         
    if counter==10:
        print("\n")
        counter=0
        

