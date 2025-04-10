import random, os, time

inventory = []

try:
	f = open("inventory.txt", "r")
	inventory = eval(f.read())
	f.close()
except:
	pass

def add():
	time.sleep(1)
	os.system("cls")
	print("Inventory")
	print("=========")
	print()
	item = input("Item to add: ").capitalize()
	inventory.append(item)
	print("Added")

def view():
	time.sleep(1)
	os.system("cls")
	print("Inventory")
	print("=========")
	print()
	seen = set(inventory)
	for item in seen:
		print(f"{item} {inventory.count(item)}")
	time.sleep(1)

def remove():
	time.sleep(1)
	os.system("cls")
	print("Inventory")
	print("=========")
	print()
	item = input("Item to remove: ").capitalize()
	if item in inventory:
		inventory.remove(item)
		print("Removed")
	else:
		print("You don't have it here.")

while True:
	time.sleep(1)
	os.system("cls")
	print("Inventory")
	print("=========")
	menu = input("Enter... \n1 Add \n2 View \n3 Remove\n> ")
	if menu == "1":
		add()
	elif menu == "2":
		view()
	elif menu == "3":
		remove()
	f = open("inventory.txt", "w")
	f.write(str(inventory))
	f.close()