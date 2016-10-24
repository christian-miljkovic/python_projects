# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #10



# Part 2

import random

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
    
# ask user for phrase

phrase=input("Enter a phrase: ")

# take out the punctuation using for loop

clean_phrase=""

for c in range(len(phrase)):
    if phrase[c].isspace()==True:
        clean_phrase+=phrase[c]

    elif phrase[c].isalpha()== True:
        clean_phrase+=phrase[c]        

clean_phrase2=clean_phrase.lower()

# split into a list in order to change key words

phrasesplit=clean_phrase2.split(" ")


# switch key words and capitalize those words

for i in range(len(phrasesplit)):

    if phrasesplit[i] in Roget_Thesaurus:
        random_num=random.randint(0,(len(Roget_Thesaurus[phrasesplit[i]])-1))
        
        phrasesplit[i]=Roget_Thesaurus[phrasesplit[i]][random_num].upper()


# convert back to string
str_phrase=""
for i in range(len(phrasesplit)):
    str_phrase+=phrasesplit[i]+" "


print(str_phrase)

