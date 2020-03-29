#! /usr/bin/python3
import os.path
import os
import pickle

# empty array for dog feeding
dogsFeeding = []

# asks users for the dogs name then shows its feeding
def getFeeding(DF):
	found = False
	n = 0
	f = 0
	PATH = "/home/skelly/Scripting/FeedingProgram/feeding.data"
	if os.path.isfile(PATH):
		print("Please enter a dogs name, I will display it's feeding.")
		with open("feeding.data", "rb") as file:
			DF = pickle.load(file)
			# print(DF)
			userInput = input(">>")
			while not found:
				if userInput == DF[n][f]:
					found = True
					print("-----------------------------")
					print("| Feeding amount: ", DF[n][f+1], " cups.|")
					print("-----------------------------\n")
					input(">>")
					menu()
				else:
					n = n+1
		input(">>")
	else:
		input(">>")
		menu()

# lists all of the current dogs and feedings on file
def listFeeding():
	os.system("clear")
	i = 0
	with open("feeding.data", "rb") as dogFile:
		DF = pickle.load(dogFile)
		print(" NAME | CUPS")
		print("-------------")
		for i in range(len(DF)):
			print(DF[i], "\n")
		input(">>")
		menu()

# this is used only to create a new feeding file (first run)
# NOW OBSOLETE
def loadArray(DF):
	with open("feeding.data", "wb") as dogFile:
		pickle.dump(DF, dogFile)

# this asks the user for a new dog with its feedings then saves it to file
def addFeeding(DF):
	while True:
		os.system("clear")
		print("Type 'exit' to stop entering dogs.")
		with open("feeding.data", "rb") as dogFile:
			DF = pickle.load(dogFile)
			userInput = input("Please enter dog name:\n>>")
			if userInput == 'exit': break
			else:
				userInput2 = input("Please enter feeding amount:\nCUPS>>")
				DF.append([userInput, userInput2])
				# print(DF)
		with open("feeding.data", "wb") as dogFile:
			pickle.dump(DF, dogFile)
	menu()

def removeDog():
	os.system("clear")
	userInput = input("What dog would you like to remove?\n>>")
	found = False
	n = 0
	f = 0
	while found == False:
		with open("feeding.data","rb") as dogFile:
			DF = pickle.load(dogFile)
			print(DF[n][f])
			dog = DF[n][f]
			if userInput == dog:
				found = True
				del DF[n][f]
				del DF[n][f]
				del DF[n]
				print(DF)
				dogFile = open("feeding.data", "wb")
				pickle.dump(DF, dogFile)
				dogFile.close()
			else:
				print(DF[n])
				n = n+1
		print(userInput, " removed.\n")
		input(">>")
		menu()


# creates a brand new feeding.data doc or resets the current one
def newSave(DF):
	with open("feeding.data","wb") as newDogFile:
		pickle.dump(DF, newDogFile)
	menu()

# menu for navigation of programs features
def menu():
	os.system("clear")
	userInput = input("1. Add new feeding info\n2. Get feeding info\n3. List feeding info\n"
			  "4. Remove Dog\n5. Exit\n\n6. New save (WILL DELETE ALL DATA)\n>>")
	if userInput == "1":
		print()
		addFeeding(dogsFeeding)
	elif userInput == "2":
		print()
		getFeeding(dogsFeeding)
	elif userInput == "3":
		print()
		listFeeding()
	elif userInput == "4":
		removeDog()
	elif userInput == "5":
		exit()
	elif userInput == "6":
		userInput2 = input("To delete all data type 'delete'.\n>>")
		if userInput2 == "delete":
			newSave(dogsFeeding)
		else:
			menu()
	else:
		print("I did not understand that command.")
		menu()

# starts the program
menu()
