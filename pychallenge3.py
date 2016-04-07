#challenge3
with open("mess2") as f:
	for line in f:
		for i in range(3,len(line)):
			if line[i].islower() and line[i-1].isupper() and line[i-2].isupper() and line[i-3].isupper() and line[i-4].islower() and line[i+1].isupper() and line[i+2].isupper() and line[i+3].isupper()and line[i+4].islower():
				print line[i],