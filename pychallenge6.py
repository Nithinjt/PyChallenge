#challenge6
import zipfile
file=zipfile.ZipFile("channel.zip","r")
name="90052.txt"
count=0
o=[]
while True:
	try:
		o.append(file.getinfo(name).comment)
		name=(file.read(name).split())[3] 
		name+='.txt'
		count+=1
		
	except:		
		print name,count
		print file.read(name)
		break


print " ".join(o)		