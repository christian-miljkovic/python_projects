# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #5


# ask for the input and use data validation

while True:
    num=int(input("Enter a number to test: "))
    if num>0:
        break
    else:
        print("That is not a valid input, try again." )
        
# create accumulator variables in order to run through numbers

divisor=0
n=2

# create while loop in order to run through divisors

for i in range(2,num):
    if num%n==0:
        print(n,"is a divisor of",num,"...stopping")
        divisor+=1
        break
    else:
        print(n,"is not a divisor of",num,"... continuing")
    n+=1
        
        

print()

# create the part that uses the accumulators in order to determine whether the number is prime or not

if divisor>0:
    print(num,"is not a prime number.")

elif num%n==0:
    print(num,"is a prime number.")

else:
    print(num,"is a prime number.")
