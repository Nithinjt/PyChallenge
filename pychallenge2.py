#challenge 2
with open("mess.txt") as f:
	for line in f:
		for i in line:
			if i.isalpha():
				print i,