# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #1


#Create variables and set them equal to their respective values

speed_of_light_kps=299792.458

km_to_miles=0.621

speed_of_earth_mph=66600

#print out the variables and the words that accompany them


print("Speed of light (Kilometers / sec):    ",speed_of_light_kps,"kps")
print("Speed of light (Miles / sec):         ",speed_of_light_kps*km_to_miles,"mps")
print("Half speed of light (Miles / sec):    ",(speed_of_light_kps*km_to_miles)/2,"mps")
print("Quarter speed of light (Miles / sec): ",(speed_of_light_kps*km_to_miles)/4,"mps")
print()
print("The earth moves 66,600 miles / hour around the sun")
print("66,600 miles per hour is equal to:   ",(speed_of_earth_mph/3600)/km_to_miles, "kps")
print("66,600 miles per hour is equal to:   ",((speed_of_earth_mph/36)/km_to_miles/speed_of_light_kps), "% of the speed of light")


