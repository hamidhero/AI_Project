from ReadingFromFile import *
import urllib2
import json

def GetFromAPI(title, year):
	request = urllib2.urlopen("http://www.omdbapi.com/?t="+title+"&y="+year+"&plot=short&r=json")
	obj = json.load(request)
	return obj

dictionary = {}

for movie in array2004:
	dictionary[movie] = GetFromAPI(movie, '2004')

for movie in array2005:
	dictionary[movie] = GetFromAPI(movie, '2005')

for movie in array2006:
	dictionary[movie] = GetFromAPI(movie, '2006')

for movie in array2007:
	dictionary[movie] = GetFromAPI(movie, '2007')

for movie in array2008:
	dictionary[movie] = GetFromAPI(movie, '2008')

for movie in array2009:
	dictionary[movie] = GetFromAPI(movie, '2009')

for movie in array2010:
	dictionary[movie] = GetFromAPI(movie, '2010')

for movie in array2011:
	dictionary[movie] = GetFromAPI(movie, '2011')

for movie in array2012:
	dictionary[movie] = GetFromAPI(movie, '2012')

for movie in array2013:
	dictionary[movie] = GetFromAPI(movie, '2013')


print dictionary

