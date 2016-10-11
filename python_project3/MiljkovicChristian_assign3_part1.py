# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #3

print("Trianlge Tester")

#promt the user to enter 3 points

point1_x= float(input("Enter the x-coordinate for the first point: "))
point1_y= float(input("Enter the y-coordinate for the first point: "))

point2_x=float(input("Enter the x-coordinate for the second point: "))
point2_y=float(input("Enter the y-coordinate for the second point: "))

point3_x=float(input("Enter the x-coordinate for the third point: "))
point3_y=float(input("Enter the y-coordinate for the third point: "))

print()
#calculate the length of each side and print the value

side1= ((point1_x - point2_x)**2 + (point1_y - point2_y)**2)**0.5

side2= ((point2_x - point3_x)**2 + (point2_y - point3_y)**2)**0.5

side3= ((point3_x - point1_x)**2 + (point3_y - point1_y)**2)**0.5

#format and print

form_side1=format(side1,".2f")
form_side2=format(side2,".2f")
form_side3=format(side3,".2f")

print("The length of each side of your shape is:")

print("Side 1:",form_side1)
print("Side 2:",form_side2)
print("Side 3:",form_side3)
print()
#create if and else statement to make sure that we have a triangle based on length size

if (side1 + side2) > side3 and (side2+side3) > side1 and (side3+side1)>side2:
   print("This is a triangle.")
else:
    print("This is not a valid triangle.")
