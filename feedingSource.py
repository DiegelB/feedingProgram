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
	PATH = "/home/mlgprobei/Scripting/FeedingProgram/feeding.data"
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
					menu()
				else:
					n = n+1
	else:
		menu()

# lists all of the current dogs and feedings on file
def listFeeding():
	i = 0
	with open("feeding.data", "rb") as dogFile:
		DF = pickle.load(dogFile)
		print(" NAME | CUPS")
		print("-------------")
		for i in range(len(DF)):
			print(DF[i], "\n")
		menu()

# this is used only to create a new feeding file (first run)
# NOW OBSOLETE
def loadArray(DF):
	with open("feeding.data", "wb") as dogFile:
		pickle.dump(DF, dogFile)

# this asks the user for a new dog with its feedings then saves it to file
def saveArray(DF):
	with open("feeding.data", "rb") as dogFile:
		DF = pickle.load(dogFile)
		userInput = input("Please enter dog name:\n>>")
		userInput2 = input("Please enter feeding amount:\n>>")
		DF.append([userInput, userInput2])
		# print(DF)
	with open("feeding.data", "wb") as dogFile:
		pickle.dump(DF, dogFile)
	print()
	menu()

# creates a brand new feeding.data doc or resets the current one
def newSave(DF):
	with open("feeding.data","wb") as newDogFile:
		pickle.dump(DF, newDogFile)
	menu()

# menu for navigation of programs features
def menu():
	userInput = input("1. Add new feeding info\n2. Get feeding info\n3. List feeding info\n"
					  "4. Exit\n\n5. New save (WILL DELETE ALL DATA)\n>>")
	if userInput == "1":
		print()
		saveArray(dogsFeeding)
	elif userInput == "2":
		print()
		getFeeding(dogsFeeding)
	elif userInput == "3":
		print()
		listFeeding()
	elif userInput == "4":
		exit()
	elif userInput == "5":
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
