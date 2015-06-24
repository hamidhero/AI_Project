from BeautifulSoup import BeautifulSoup
import urllib2 
import re

resp1 = urllib2.urlopen("http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us&title_type=feature&year=2008,2008")
resp2 = urllib2.urlopen("http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us&start=51&title_type=feature&year=2008,2008")
resp3 = urllib2.urlopen("http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us&start=101&title_type=feature&year=2008,2008")
resp4 = urllib2.urlopen("http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us&start=151&title_type=feature&year=2008,2008")
resp5 = urllib2.urlopen("http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us&start=201&title_type=feature&year=2008,2008")
resp6 = urllib2.urlopen("http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us&start=251&title_type=feature&year=2008,2008")
resp7 = urllib2.urlopen("http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us&start=301&title_type=feature&year=2008,2008")
resp8 = urllib2.urlopen("http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us&start=351&title_type=feature&year=2008,2008")
resp9 = urllib2.urlopen("http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us&start=401&title_type=feature&year=2008,2008")
resp10 = urllib2.urlopen("http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us&start=451&title_type=feature&year=2008,2008")

html1 = str(resp1.read())
html2 = str(resp2.read())
html3 = str(resp3.read())
html4 = str(resp4.read())
html5 = str(resp5.read())
html6 = str(resp6.read())
html7 = str(resp7.read())
html8 = str(resp8.read())
html9 = str(resp9.read())
html10 = str(resp10.read())

soup1 = BeautifulSoup(html1)
soup2 = BeautifulSoup(html2)
soup3 = BeautifulSoup(html3)
soup4 = BeautifulSoup(html4)
soup5 = BeautifulSoup(html5)
soup6 = BeautifulSoup(html6)
soup7 = BeautifulSoup(html7)
soup8 = BeautifulSoup(html8)
soup9 = BeautifulSoup(html9)
soup10 = BeautifulSoup(html10)

links = []

links.append(soup1.findAll("a", href=True))
links.append(soup2.findAll("a", href=True))
links.append(soup3.findAll("a", href=True))
links.append(soup4.findAll("a", href=True))
links.append(soup5.findAll("a", href=True))
links.append(soup6.findAll("a", href=True))
links.append(soup7.findAll("a", href=True))
links.append(soup8.findAll("a", href=True))
links.append(soup9.findAll("a", href=True))
links.append(soup10.findAll("a", href=True))


for link in links:
	for single_link in link:
		if '/title/' in str(single_link):
			if '<img' not in str(single_link) and 'vote' not in str(single_link):
				print str(single_link)[str(single_link).find('>')+1:-4]
            	
            	
        		
            	


