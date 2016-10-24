# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #5



# create while loop in order to run through divisors dont forget that range doesnt include the last number which is why you need 1001 instead of 1000


for x in range(2,1001):
    if x==2:
        print(x,"is a prime number!")
    else: 
        for i in range(2,x):
                if x%i==0:
                    break
                elif x%i!=0:
                    if i==(x - 1):
                        print(x, "is a prime number!")
        
        


