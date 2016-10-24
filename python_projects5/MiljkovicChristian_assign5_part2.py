# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #5

# ask teacher for number of students in class and tests with data validation

while True:
    num_students=int(input("How many students are in your class? "))
    if num_students>0:
        break
    else:
        print("Invalid number of students, try again.")

while True:
    num_tests=int(input("How many tests in this class? "))
    if num_tests>0:
        break
    else:
        print("Invalid number of tests, try again.")
print()
print("Here we go!")
print()

# hold scores in accumulator variable

all_student_score=0
student_total=0
total_avg=0
a=1

# create a for loop to run through each student

for i in range(1,num_students+1):
    print("****Student #",end="")
    print(i,"****")
    

# create accumulator for each student to calculate their average score
    student_total=0
    
    
    for i in range(1,num_tests+1):

        i=str(i)
        question="Enter score for test #"+i+": "
        
        while True:
# the i=str(i) is important allows me to concatenate the students number in the input since input requires a string
            test_score=int(input(question))

            if test_score>0:
                student_total+=test_score
                break
                
            elif test_score<0:
                print("Invalid score, try again.")
                
                
    

# calculate then print the average score for each student and add this to the student total accumulator

    avg_student=student_total/num_tests
    total_avg+=avg_student
    i=str(i)
    print("Average score for student #"+i+" is:",format(avg_student,".2f"))

# calculate the entire average for the class
print()
class_avg=total_avg/(num_students)
print("Average score for all students is:",format(class_avg,".2f"))


