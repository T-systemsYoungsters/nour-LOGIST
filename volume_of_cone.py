from math import *

print("Volume of a cone")

height = float(input("Enter the height of the cone : "))
radius = float(input("Enter the radius of the cone : "))

volume = (pi * radius**2 *height) / 3

print("The volume is : ",volume)
