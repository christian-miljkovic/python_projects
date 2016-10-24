# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #10


# Part 3 extra credit

import random

# define a location for our file

# select a class file

filename="bieber_baby.txt"


# open the file
try:
    myfile= open(filename,"r")
    
except:
    print("File cannot be opened")

# grab all the data as a string
else:
    alldata= myfile.read()

# close the file
    myfile.close()

    # clean the lyrics

    clean_lyrics=""

    for c in range(len(alldata)):
        if alldata[c].isspace()==True:
            clean_lyrics+=alldata[c]

        elif alldata[c].isalpha()== True:
            clean_lyrics+=alldata[c]        

    clean_lyrics2=clean_lyrics.lower()

    # split lines into a list

    lines=clean_lyrics2.split("\n")

    # get rid of line breaks using for loop

    while '' in lines:
        location= lines.index('')
        del lines[location]
                    

    # split lines into just single words ***remeber to use a for loop for these kind of parts
    lyrics=[]
    for i in range(len(lines)):
        splitlines=lines[i].split(" ")
        
        for i in range(len(splitlines)):
            single_words=splitlines[i].split(" ")

            lyrics+=single_words


# Put in the Roget Theusaurs

# define a location for our file

# select a class file

filename="Roget_Thesaurus.txt"


# open the file
try:
    myfile= open(filename,"r")
    
except:
    print("File cannot be opened")

# grab all the data as a string
else:
    alldata= myfile.read()

# close the file
    myfile.close()

    # turn the string into a list
    lines = alldata.split("\n")



# create a new dictionary for the Roget Thesaurus

Roget_Thesaurus={}


# turn each list into a key and the synonmys
    
for i in range(len(lines)):

    splitlines=lines[i].split(",")
    val_list=[]
    
    for c in range(1,len(splitlines)):
        val_list.append(splitlines[c])

        Roget_Thesaurus[splitlines[0]]=val_list


# ask the user for percent chance to change a word

chance=float(input("Enter a % chance to change a word (i.e. 0.5 for 50%): "))
print()

num=int(chance*10)

random_num=random.randrange(num,11,num)



# switch key words and capitalize those words

for i in range(len(lyrics)):

    random_num=random.randrange(num,11,num)
   
    if lyrics[i] in Roget_Thesaurus:

        if random_num==num:
        
            random_num2=random.randint(0,(len(Roget_Thesaurus[lyrics[i]])-1))
            
            lyrics[i]=Roget_Thesaurus[lyrics[i]][random_num2].upper()


# convert back to string
str_lyrics=""
for i in range(len(lyrics)):
    str_lyrics+=lyrics[i]+" "

print(str_lyrics)
