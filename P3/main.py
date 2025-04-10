import os, time, random

toDoList = []

def add():
	time.sleep(1)
	os.system('cls')
	item = input("What would you like to add\n> ")
	date = input("What is the due date> ")
	priority = input("What is the priority(high, medium, low)> ").capitalize()
	row = [item, date, priority]
	toDoList.append(row)
	print("Added")

def view():
	time.sleep(1)
	os.system('cls')
	option = input("Enter... \n1 to view all tasks\n2 to view tasks by priority\n> ")
	if option == "1":
		for row in toDoList:
			for item in row:
				print(item, end=" | ")
			print()
	elif option == "2":
		priority = input("What priority do you want to see> ").capitalize()
		for row in toDoList:
			if priority in row:
				for item in row:
					print(item, end=" | ")
				print()
			print()

def remove():
	time.sleep(0.5)
	os.system('cls')
	find = input("What would you like to remove\n> ")
	for row in toDoList:
		if find in row:
			toDoList.remove(row)

def edit():
	time.sleep(0.5)
	os.system('cls')
	find = input("What would you like to edit\n> ")
	found = False
	for row in toDoList:
		if find in row:
			found = True
	if not found:
		print("Couldn't find that")
		return
	for row in toDoList:
		if find in row:
			toDoList.remove(row)
	item = input("What do you want to add\n> ")
	date = input("What is the due date> ")
	priority = input("What is the priority(high, medium, low)> ").capitalize()
	row = [item, date, priority]
	toDoList.append(row)
	print("Added")

while True:
	menu = input("Enter... \n1. Add\n2. View\n3. Remove\n4. Edit\n> ")
	if menu == "1":
		add()
	elif menu == "2":
		view()
	elif menu == "3":
		remove()
	elif menu == "4":
		edit()
	time.sleep(1)
	os.system('cls')