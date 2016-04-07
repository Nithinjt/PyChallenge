#challenge4
import urllib
nthng='12345'
j=0
while j<400:
	site=urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nthng)
	data=site.read()
	data=data.split()
	for count,i in enumerate(data):
		if count==5:
			nthng=i
			print i
			