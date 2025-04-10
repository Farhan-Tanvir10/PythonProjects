import os

with open("high.score", "r") as f:
	scores = f.readlines()

	highscore = 0
	name = None

for row in scores:
	date = row.strip().split()
	if date:
		try:
			score = int(date[1])
			if score > highscore:
				highscore = score
				name = date[0]
		except ValueError:
			print(f"Invalid score: {date[1]}")

if name is not None:
	print(f"The winner is {name} with {highscore}.")
else:
	print("No valid scores found.")