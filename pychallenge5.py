#challenge5
import pickle
import urllib
site=urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data=pickle.load(site)
#print data
#'\n'.join([''.join([p[0] * p[1] for p in row]) for row in data])
for line in data:
    print ''.join(elmt[0] * elmt[1] for elmt in line)