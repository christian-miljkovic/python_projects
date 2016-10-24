# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #7


############ Part A




# import random mod and strings so that you can randomly generate a letter

import string
string.ascii_letters # this generates all of the ASCII letters
import random

# function:   add_letters
# input:      a word to scramble (String) and a number of letters (integer)
# processing: adds a number of random letters (A-Z; a-z) after each letter 
#             in the supplied word. for example, if word="cat" and num=1 
#             we could generate any of the following:
#             cZaQtR
#             cwaRts
#             cEaett
# 
#             if word="cat" and num=2 we could generate any of the following:
#             cRtaHFtui
#             cnnaNYtjn
#             czAaAitym
#
# output:     returns the newly generated word



def add_letters(word, num):

# accumulators for concatenating the strings
    encoding_character=string.ascii_letters+string.punctuation # uses punctuation and all ascii letters

    new_word=""
    rando_num=""
    counter=0

    for i in range(len(word)):
        
        # for loop in order to create a certain number of encoding characters

        while counter<num:
            rando_num+=random.choice(encoding_character)
            counter+=1
            
        new_word+=word[i]+rando_num

    
    return new_word

###########################





        


# function:   remove_letters
# input:      a word to unscramble (String) and the number of characters to remove (integer)
# processing: the function starts at the first position in the supplied word and keeps it.
#             it then removes "num" characters from the word. the process is repeated again
#             if the word contains additional characters - the next character is kept
#             and "num" more characters are removed.  For example, if word="cZaYtU" and
#             num=1 the function will generate the following:
#        
#             cat (keeping character 0, removing character 1, keeping character 2, removing
#                  character 3, keeping character 4, removing character 5)
#
# output:     returns the newly unscrambed word


def remove_letters(word, num):

# create unscrambling accumulator

    unscrambler=""

    for i in range(0,len(word),num+1): # step aspect of range 1 means youre going one at a time 2 is skipping every other
        unscrambler+=word[i]

    return unscrambler

############################







    
 # function:   shift_characters
# input:      a word (String) and a number of characters to shift (integer)
# processing: shifts each character in the supplied word to another position in the ASCII
#             table. the new position is dictated by the supplied integer.  for example,
#             if word = "apple" and num=1 the newly generated word would be:
#
#             bqqmf
#
#             because we added +1 to each character. if we were to call the function with
#             word = "bqqmf" and num=-1 the newly generated word would be:
#           
#             apple
#
#             because we added -1 to each character, which shifted each character down by
#             one position on the ASCII table.
#
# output:     returns the newly generated word



def shift_characters(word, num):

# accumulator for concatenation

    shifted_word=""
    
    for i in range(len(word)):
        if num>0:
            shifted_word+=chr(ord(word[i])+num)
        else:
            shifted_word+=chr(ord(word[i])-(num*-1))


    return shifted_word


#################### Part B


# ask user what they want to do to the set of characters

choice_operation=input("(e)ncode, (d)ecode or (q)uit: ")


# encoding part

if choice_operation=="e":

# data validation while also asking user for certain amount of numbers to encode


    while True:
        num=int(input("Enter a number between 1 and 5: "))

        if num<=0:
            print("That is not a valid choice of number.")
            continue

        else:
            break


    word=input("Enter a phrase to encode: ")

# use add letters function

    word=add_letters(word, num)

# use shift characters function

    encoded_word=shift_characters(word, num)

    print("Your encoded word is:",encoded_word)

    
# decoding part   
        
elif choice_operation=="d":

# data validation while also asking user for certain amount of numbers to decode


    while True:
        num=int(input("Enter a number between 1 and 5: "))

        if num<=0:
            print("That is not a valid choice of number.")
            continue

        else:
            break   
    
# ask for phrase to decode

    word=input("Enter a phrase to decode: ")

# use the remove function

    word=remove_letters(word, num)

# use the shift runction

    decoded_word=shift_characters(word,(num*-1))

    print("Your decoded word is:",decoded_word)
    

# quit part

else:
    print("Ending program.")


        
















        

        
