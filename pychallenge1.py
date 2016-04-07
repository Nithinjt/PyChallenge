#challenge 1
n=raw_input()
from string import *
k=maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
print n.translate(k)'''

'''
#challenge 2
with open("mess.txt") as f:
	for line in f:
		for i in line:
			if i.isalpha():
				print i,