# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #7

# Part 1a


# create accumulators for the requirements in username

upper=0
lower=0
digit=0


while True:
    username=input("Please enter a username: ")

# create a variable in order to index the last character

    a=int(len(username))-1

# check if there are non characters in the username

    non_char=str.isalnum(username)

# check if there are digits in the first char

    non_dig1=username[0].isnumeric()

# check if there is a digit in the last char

    non_dig2=username[a].isnumeric()

# check if there are digits in the first and last

    first_num=ord(username[0])
    last_num=ord(username[a])
    
# check if the username contains at least one uppercase,lower,and digit char 


    for c in username:
        if c.isdigit():
            digit+=1

        if c.isupper():
            upper+=1

        if c.islower():
            lower+=1
        


    if len(username)>15:
        print("Password must be less than 15 characters long")
        print()
        continue

    elif len(username)<5:
        print("Password must be more than 5 characters long")
        print()
        continue

    elif non_char==False:
        print("Password can only contain alphabetic and numeric characters")
        print()
        continue

    elif non_dig1==True:
        print("The first character cannot be a digit")
        print()
        continue

    elif non_dig2==True:
        print("The last character cannot be a digit")
        print()
        continue 

    elif digit<1:
        print("Password must have at least 1 number in it")
        print()
        continue

    elif upper<1:
        print("Password must have at least 1 uppercase letter in it")
        print()
        continue

    elif lower<1:
        print("Password must have at least 1 lower case letter in it")
        print()
        continue
          

    else:
        break

print("Your username is valid!")
print()


#### Part 1b





while True:


    
    password=input("Please enter a password: ")

# check if the password contains at least one uppercase,lower,and digit char 


### create accumulator varibales for password requirements

    digits2=0
    upper2=0
    lower2=0
    special_char=0
    space=0
    invalid_char=0

    for c in password:
        if c.isdigit():
            digits2+=1

        elif c.isupper():
            upper2+=1

        elif c.islower():
            lower2+=1

        elif ord(c)==35:
            special_char+=1

        elif ord(c)==36:
            special_char+=1
                
        elif ord(c)==37:
            special_char+=1

        elif ord(c)==38:
            special_char+=1    
            
        else:
            invalid_char+=1        

# check if the username have the password in it

    a=0 # this variable is for the replication of the username in password

    replicant=password.count(username)

    if replicant>0:
        a+=1
        


    if len(password)<8:
        print("Password must be more than 8 characters long")
        print()
        continue
    
    elif a>0:
        print("You cannot use your username as part of your password")
        print()
        continue

    elif invalid_char>0:
        print("There is at least one invalid character in your password")
        print()
        continue


    elif space>0:
        print("There can be no spaces in the password")
        print()
        continue


    elif digits2<1:
        print("Password must have at least 1 number in it")
        print()
        continue

    elif upper2<1:
        print("Password must have at least 1 uppercase letter in it")
        print()
        continue

    elif lower2<1:
        print("Password must have at least 1 lower case letter in it")
        print()
        continue

    elif special_char<1:
        print("Password must have at least 1 special character in it")
        print()
        continue         

    else:
        break


print("Your password is valid!")

