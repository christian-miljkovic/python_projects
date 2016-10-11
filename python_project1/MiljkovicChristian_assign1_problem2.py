# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #1

#Input of names into respective variables

name1= input("Please enter name #1: ")
name2= input("Please enter name #2: ")
name3= input("Please enter name #3: ")

#print space between input of varibales then the header

print()
print("Here are your names in every possible order:")
print("--------------------------------------------")
print()
#Output of names with formatting

print("1.",end=" ")
print(name1,name2,name3,sep=", ")
print()
print("2.",end=" ")
print(name1,name3,name2,sep=", ")
print()
print("3.",end=" ")
print(name2,name1,name3,sep=", ")
print()
print("4.",name2)
print(name3)
print(name1)
print()
print("5.",name3)
print(name2)
print(name1)
print()
print("6.",name3)
print(name1)
print(name2)
