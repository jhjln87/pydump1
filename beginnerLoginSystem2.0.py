# Login System
import time
users = ["Atusiff","Moretusiff","Lookotza","user","firewater","SusanWojcicki","Alexander","coinJar"]
password = ["lampShade","lampshade2","Lookotza","pass","789","YouTube","iAmCEO","clink"]

while True:
	action = input("Login or Register? ")
		
	if action == "Register" or action == "register":
		users = [users,input("Choose username? ")]
		password = [password,input("Choose password? ")]
		time.sleep(0.5)
		print("Added")
		
	if action == "Login" or action == "login":
		inputUser = input("Username: ")
		inputPass = input("Password: ")
		time.sleep(0.5)
		print(" ")

		if inputUser in users:
			id = users.index(inputUser)
			if password[id] == inputPass:
				print("Welcome",inputUser)
			else:
				print("Incorrect password")
		else:
			print("User not detected")
	for x in range(0,3):
		time.sleep(0.5)
		print(" ")