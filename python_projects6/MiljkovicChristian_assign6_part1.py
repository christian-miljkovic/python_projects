# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #6



# function:   compute_area_of_rectangle
# input:      length (integer) and width (integer)
# processing: computes the area of the described rectangle
# output:     returns the area of the described rectangle (integer)

def compute_area_of_rectangle(length, width):
    area=length*width
    return area

# function:   compute_perimeter_of_rectangle
# input:      length (integer) and width (integer)
# processing: computes the perimeter of the described rectangle
# output:     returns the perimeter of the described rectangle (integer)

def compute_perimeter_of_rectangle(length,width):
    perimeter=2*length+2*width
    return perimeter

# function:   draw_rectangle
# input:      length (integer) and width (integer)
# processing: draws the rectangle using a series of "*" characters (see below for a sample 4 by 3 rectangle:)
#             ***
#             ***
#             ***
#             ***
# output:     returns nothing

def draw_rectangle(length,width):

    for i in range(length):
        print("*" * width)

# function:   get_input
# input:      a prompt to ask the user (String), a low value (integer) and a high value (integer)
# processing: continually prompts the user with the supplied prompt for an integer. if the
#             user does not supply an integer within the defined range the function will re-prompt them
# output:     returns the integer the user supplied


def get_input(prompt,low,high):

    while True:
        answer = int(input(prompt))
        if answer < low or answer > high:
            print("Try again")
        else:
            break
        
    return answer

##########



length = get_input("Enter a length between 3 and 10", 3, 10)
width  = get_input("Enter a width between 3 and 10", 3, 10)

area  = compute_area_of_rectangle(length, width)
perim = compute_perimeter_of_rectangle(length, width)

print ("Area:", area, "; Perim:", perim)

draw_rectangle(length, width)


