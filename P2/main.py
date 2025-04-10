import os, time, random

bingo = []

def ran():
	number = random.randint(1, 90)
	return number

def prettyPrint():
	for row in bingo:
		for item in row:
			print(item, end="\t|\t")
		print()

def createCard():
	global bingo
	numbers = []
	for i in range(8):
		num = ran()
		while num in numbers:
			num = ran()
		numbers.append(num)
		
	numbers.sort()

	bingo = [
		[numbers[0], numbers[1], numbers[2]],
		[numbers[3], "Bingo" ,numbers[4]],
		[numbers[5], numbers[6], numbers[7], ]
	]
	
createCard()

while True:
	os.system("cls")
	prettyPrint()
	number = int(input("Enter a number: "))
	for row in range(3):
		for item in range(3):
			if bingo[row][item] == number:
				bingo[row][item] = "X"

	exes = 0
	for row in bingo:
		for item in row:
			if item == "X":
				exes += 1

	if exes == 8:
		print("You win!")
		break

	time.sleep(1)
	os.system("cls")