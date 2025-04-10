import os, time, random

listOfWords = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
letterPicked = []
lives = 6

word = random.choice(listOfWords)

while True:
	time.sleep(1)
	os.system("cls")
	print("Welcome to Hangman!")
	letter = input("Enter a letter: ").lower()
	if letter in letterPicked:
		print("You already picked that letter!")
		continue
	letterPicked.append(letter)

	if letter in word:
		print("You've found a letter!")
	else:
		print("Nope, not in there!")
		lives -= 1

	allLetters = True
	print()
	for i in word:
		if i in letterPicked:
			print(i, end="")
		else:
			allLetters = False
			print("_", end="")

	print()

	if allLetters:
		print(f"You have won with {lives} lives remaining!")
		break

	if lives <= 0:
		print(f"You have run out of lives. The correct answer was {word}.")
	else:
		print(f"You have {lives} lives remaining!")
	time.sleep(1)
	os.system("cls")