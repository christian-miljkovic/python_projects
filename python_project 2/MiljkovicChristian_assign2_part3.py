# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #2


#ask user for thier name and store it

student_name= input("What is your name? ")


#ask the user for the name of their class and store it

class_name = input("What class are you in? ")
print()



#ask the user the weighting of the test of their class

test_weight= float(input("What is the weighting of tests in this class (i.e. 0.40): "))


#ask the user for 3 test scores then calculate the students average, format then print it

test1= float(input("Enter your grade for the first test: "))
test2= float(input("Enter your grade for the second test: "))
test3= float(input("Enter your grade for the third test: "))

test_avg= (test1+test2+test3)/3

clean_test_avg= format(test_avg,".2f")

print()
print("Your test average is: ", clean_test_avg)
print()

#ask the user for the weigting of homework assignments

hw_weight= float(input("What is the weighting of homeworks in this class (i.e. 0.40): "))


#ask the user for 3 homework assignment scores then calculate the students homework average, format then print it

hw1= float(input("Enter your grade for the first homework assignment: "))
hw2= float(input("Enter your grade for the second homework assignment: "))
hw3= float(input("Enter your grade for the third homework assignment: "))

hw_avg= (hw1+hw2+hw3)/3

clean_hw_avg= format(hw_avg,".2f")

print()
print("Your homework average is:",clean_hw_avg)
print()

#calculate the students final grade, format then print it

final_grade = (test_weight*test_avg)+(hw_weight*hw_avg)

clean_final_grade= format(final_grade,".2f")

print("Thanks,",student_name, end=". ")
print("Your final score in",class_name,"is",clean_final_grade)
