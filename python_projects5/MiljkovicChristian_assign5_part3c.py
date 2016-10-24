# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #5

# ask for the user (using data validation) for a valid start and end point to determine whether there are prime numbers within the range

while True:
    a= int(input("Start number: "))
    b=int(input("End number: "))

    if (a<=0) or (b<=0):
        print("Start and end must be positive.")
        print()
        continue
    elif a>=b:
        print("End number must be greater than start number.")
        print()
    else:
        print()
        break



# create the same while loop from part 2 in order to run through divisors dont forget that range doesnt include the last number which is why you need 1001 instead of 1000


for x in range(a,b+1):
    if x==2:
        print(x,"is a prime number!")
    else: 
        for i in range(2,x):
                if x%i==0:
                    break
                elif x%i!=0:
                    if i==(x-1):
                        print(x, "is a prime number!")
        
