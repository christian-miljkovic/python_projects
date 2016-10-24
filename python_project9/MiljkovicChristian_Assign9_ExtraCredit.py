# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #9 extra credit

import urllib.request

import turtle


while True:

    # select a class file

    image_name=input("Enter a an image filename: ")

    # define a location for our file

    url="http://cs.nyu.edu/~kapp/python/"+image_name+".txt"
    
    try:

        # initiate request to URL
        response=urllib.request.urlopen(url)

        # read data from URL as a string
        data=response.read().decode('utf-8')
        print("Success! I was able to find","'"+url+"'")
        # split data and convert integers and put them in a new list

        splitdata=data.split(",")

        length=int(splitdata[0])
        width=int(splitdata[1])
        color=float(splitdata[2])
        break

    except:
        print("Sorry,",url,"doesn't exist.")


        
# set a title for canvas window

turtle.title("Image Parser")

# set up screen
turtle.setup(length,width)

# position

xpos=length//2
ypos=width//2

# create function in order to make a box

def box(width,length):

    turtle.penup()
    turtle.goto(xpos,ypos)
    turtle.pendown()
    turtle.left(180)
    turtle.forward(width)
    
    for i in range(3):
        turtle.left(90)
        turtle.forward(width)



    
       
# draw the gray background

turtle.pencolor(color,color,color)
turtle.fillcolor(color,color,color)
turtle.begin_fill()
box(width,length)
turtle.end_fill()



turtle.exitonclick()



    

