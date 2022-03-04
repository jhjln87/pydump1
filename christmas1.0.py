import time
import random

smallBox = ["book", "T-shirt",  "movie", "piece of jewelry", "tie", "watch", "bag of candy" "smartphone", "pair of socks"] # 9
mediumBox = ["computer", "clock", "board game", "chair", "slow cooker", "bullet blender", "remote controlled truck", "trip to the movies"] # 8
bigBox = ["television", "new bed", "car", "piano", "bike", "vacation"] # 6

while True:
	answer = input("Would you like to open a present? ")
	
	if answer == "no" or answer == "No" or answer == "N" or answer == "n":
		quit()
	
	if answer == "yes"  or answer == "Yes" or answer == "Y" or answer == "y":
		type = input("What present would you like to open? (small, medium, big) ")
		for x in range(0,3):
			time.sleep(0.5)
			print(" ")

		if type == "small" or type == "Small" or type == "S" or type == "s":
			rand = random.randint(0,8)
			print("You got a(n)", smallBox[rand])
			
		if type == "medium" or type == "Medium" or type == "M" or type == "m":
			rand = random.randint(0,2)
			if rand == 2:
				rand2 = random.randint(0,8)
				rand3 = random.randint(0,8)
				print("You got a(n)", smallBox[rand2], "and a(n)", smallBox[rand3])
			if rand == 0 or rand == 1:	
				rand = random.randint(0,7)
				print("You got a(n)", mediumBox[rand])
			
		if type == "big" or type == "Big" or type == "B" or type == "b":
			rand = random.randint(0,5)
			print("You got a(n)", bigBox[rand])
print(" ")