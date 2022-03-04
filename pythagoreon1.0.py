import math
print("You are at 0,0")
print("You live at 12,3")
ans = input("Do you want to go somewhere else before your house?")

dist = math.sqrt(12*12+3*3)
if ans == "n" or ans == "no" or ans == "No":
	print("You will have to travel",dist)

if ans == "y" or ans == "yes" or ans == "Yes":
	x = int(input("What is the x value of place?"))
	y = int(input("What is the y value of palce?"))
	dist2 = (x*x+y*y+dist)
	print("You will have to travel",dist2)	