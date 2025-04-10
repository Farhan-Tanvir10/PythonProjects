import os, time, random

pizza = []

try:
	f = open("pizza.txt", "r")
	pizza = eval(f.read())
	f.close()
except:
	print("No such file exists yet.")

def addPizza():
	time.sleep(1)
	os.system("cls")
	name = input("Enter the name of the pizza: ")
	topping = input("Topping: ")
	size = input("Do you want it small, medium, or large(s/m/l): ").lower()
	while True:
		try:
			qty = int(input("How many do you want: "))
			break
		except:
			print("Please enter a number.")
	price = 0
	if size == "s":
		price = 5.99
	elif size == "m":
		price = 9.99
	elif size == "l":
		price = 14.99
	total = round(price * qty, 2)

	row = [name, topping, size, qty, total]
	pizza.append(row)
	print("Order taken.")

def viewPizza():
	h1 = "name"
	h2 = "topping"
	h3 = "size"
	h4 = "qty"
	h5 = "total"
	print(f"{h1:^10}{h2:^10}{h3:^10}{h4:^10}{h5:^10}")
	for row in pizza:
		print(f"{row[0]:^10}{row[1]:^10}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
		time.sleep(1)

while True:
	time.sleep(1)
	os.system("cls")
	print("Rominos Pizza")
	print()
	menu = input("Enter... \n1 Add\n2 View\n> ")
	if menu == "1":
		addPizza()
	elif menu == "2":
		viewPizza()
	f = open("pizza.txt", "w")
	f.write(str(pizza))
	f.close()