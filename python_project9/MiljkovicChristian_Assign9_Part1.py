# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #9


# answer key for part 3

answerkey = ["B","A","D","D","C","B","D","A","C",'C','D','B','A','B','A','C','B','D','A','C','A','A','B','D',"D"]


# select a class file

filename=input("Enter a filename: ")

# open the file
try:
    myfile= open(filename + ".txt","r")
except:
    print("File cannot be opened")

# grab all the data as a string
else:
    alldata= myfile.read()

# close the file
    myfile.close()

    # turn the string into a list
    lines = alldata.split("\n")

    # count the number of students
    total_students= len(lines)

    print("**** ANALYZING ****")
    print()
# examine each student record item is a single student record as string



    # create an accumulator for valid & invalid lines of data in the file
    valid_lines=0
    invalid_lines=0

    # create accumulator for points and list in order to store the values for each student
    points_accum=[]
    n_numbers=[]

    for item in lines:
        split_lines= item.split(",")

        # check length of string
        if len(split_lines)!=26:
            print("Invalid line of data: Invalid record, not enough or too many elements")
            print(item)
            invalid_lines+=1
            print()

        else:
            # check that the N is long enough

            if len(split_lines[0])!=9:
                print("Invalid line of data: Invalid N number, too long or short")
                print(item)
                invalid_lines+=1
                print()

            else:


                # check if it has a N first
                
                if split_lines[0][0]!="N":
                    print("Invalid line of data: Invalid N number")
                    print(item)
                    invalid_lines+=1
                    print()

                else:

                    # check that the rest of the N number are numerals

                    if split_lines[0][1:8].isnumeric()==False:
                        print("Invalid line of data: Invalid N number")
                        print(item)
                        invalid_lines+=1
                        print()


                    else:
                        valid_lines+=1

                        # make the item string into a list without commas

                        item_list=item.split(",")

                        # take out the N number in order to compare lists with the same length

                        clean_list=item_list[1:27]

                        n_numbers.append(item[0:9])




                        
                        # iterate through the valid lines and see how many correct answers there are

                        points=0
                        
                        for i in range(len(answerkey)):
                            

                            if answerkey[i]==clean_list[i]:
                                points+=4


                            elif str(clean_list[i]).isalnum()==False:
                                points+=0
                                

                            else:
                                points-=1
    
                        points_accum+=[points]


                        # take the list of points accumulated and figure out which is the mode
                        
                        unique_list=[]
                        num_unique=[]
                        

                        
                        for j in range(len(points_accum)):
                            mode=0

                            for k in range(len(points_accum)):

                                if points_accum[j]==points_accum[k]:
                                    mode+=1

                                    if mode>1:
                                        unique_list.append(points_accum[j])
                                        num_unique.append(mode)

                                   
#create this duplicate in order to use points_accum for later applications
                        
points_accum2=sorted(points_accum)
                        
# calculate the median
                       
if len(points_accum)%2 != 0:
    indexing=(len(points_accum2)+1)//2
    median=points_accum2[indexing-1]                           

elif len(points_accum)%2 == 0:
    median_half1=points_accum2[(len(points_accum2)//2)]
    median_half2=points_accum2[((len(points_accum2)//2)-1)]
    median=(median_half1+median_half2)/2
    
                          
                           
                           
# calculate the mode here
real_mode=[]

max_mode=max(num_unique)


for num in range(len(num_unique)):

    
    if (num_unique[num]==max_mode) and (unique_list[num] not in real_mode):
            real_mode+=[unique_list[num]]
                                    
                              
                           
                      
# compute the statistics

avg_points=sum(points_accum)/(len(points_accum))
clean_avg=format(avg_points,".2f")
highest_score=max(points_accum)
lowest_score=min(points_accum)
range_points=highest_score-lowest_score

# format the mode incase there are multiple
str_mode=""
for c in range(len(real_mode)):
    str_mode+=" " + (str(real_mode[c]))

                     

print("**** REPORT ****")
print()
print("Total valid lines of data:",valid_lines)
print("Total invalid lines of data:",invalid_lines)
print()
print("Mean (average) score:",clean_avg)
print("Highest score:",highest_score)
print("Lowest score:",lowest_score)
print("Range of scores:",range_points)
print("Median score:", median)
print("Mode score(s):",str_mode)


# see if the user wants to curve the grades




curve_question=input("Would you like to apply a curve to the scores? (y)es or (n)o? ")

if curve_question=="y":

    curve_num=int(input("Enter desired mean score: "))

    clean_avg2=float(clean_avg)
    
    curve=curve_num-clean_avg2
    

    
elif curve_question=="n":
    print("Have a nice day.")


# N numbers



# Part 5

# create a new file

# title

if curve_question=="n":
    str_name=str(filename)+"_grades.txt"

elif curve_question=="y":
    str_name=str(filename)+"_grades_with_curve.txt"
    


file_object= open(str_name,'w')

# write into the new file


if curve_question=="n":

    for i in range(len(points_accum)):

        str_input=str(n_numbers[i])+","+str(points_accum[i])+"\n"
        
        file_object.write(str_input)

elif curve_question=="y":

    for i in range(len(points_accum)):

        str_curve=points_accum[i]+curve

        clean_curve=format(str_curve,".2f")

        str_input=str(n_numbers[i])+","+str(points_accum[i])+","+clean_curve+"\n"
        
        file_object.write(str_input)
    
                
# close file

file_object.close()
          

