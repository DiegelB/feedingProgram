#! /usr/bin/python3
import os.path
import os
import pickle

dogsFeeding = []

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
def loadArray(DF):
	with open("feeding.data", "wb") as dogFile:
		pickle.dump(DF, dogFile)

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
	
def newSave(DF):
	with open("feeding.data","wb") as newDogFile:
		pickle.dump(DF, newDogFile)
	menu()
			
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
		

menu()
