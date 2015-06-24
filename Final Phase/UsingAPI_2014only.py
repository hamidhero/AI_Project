from ReadingFromFile import *
import urllib2
import json

def GetFromAPI(title, year):
	request = urllib2.urlopen("http://www.omdbapi.com/?t="+title+"&y="+year+"&plot=short&r=json")
	obj = json.load(request)
	return obj

dictionary = {}

for movie in array2014:
	dictionary[movie] = GetFromAPI(movie, '2014')


print dictionary


