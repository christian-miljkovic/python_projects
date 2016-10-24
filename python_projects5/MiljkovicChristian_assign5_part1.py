# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #5


# using data validation ask for how many beers on the wall

while True:
    beers=int(input("How many bottles of beer on the wall? "))
    if beers>0:
        break
    else:
        print("Sorry,thats not a valid number of bottles. Try again.")

print()
# create for loop to have the number of beers looped

for i in range(beers,1,-1):
    print(i,"bottles of beer on the wall,",i,"bottles of beer.","\n","Take one down, pass it around,",i-1,"bottles of beer on the wall.")
    print()

print("1 bottle of beer on the wall, 1 bottle of beer.","\n","Take one down, pass it around, no more bottles of beer on the wall.")
        
    
