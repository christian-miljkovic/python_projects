# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #10

import random


# Part 0 and 1

# define our simple thesaurus
thesaurus = {
              "happy":["glad",  "blissful", "ecstatic", "at ease"],
              "sad"  :["bleak", "blue",     "depressed"]
            }


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


# create a random integer for chosing a word out of thesaurs

num=len(thesaurus["happy"])-1

num2=len(thesaurus["sad"])-1

random_num=random.randint(0,num)

random_num2=random.randint(0,num2)



# switch key words and capitalize those words

for i in range(len(phrasesplit)):

    if phrasesplit[i]=="happy":
        phrasesplit[i]=thesaurus["happy"][num].upper()

    elif phrasesplit[i]=="sad":
        phrasesplit[i]=thesaurus["sad"][num2].upper()

# convert back to string
str_phrase=""
for i in range(len(phrasesplit)):
    str_phrase+=phrasesplit[i]+" "


print(str_phrase)

