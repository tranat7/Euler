#this script is used to get the word of the day from dictionary.com and will print the word with the definition out. 
import requests
import sys

#this is the function used to grab the source code from the websites
def getWebpage(url):
	reload(sys)
	sys.setdefaultencoding('utf-8')
	r = requests.get(url)
	return r.text

#This function will grab the word of the day based on the format. 
def getWotd():
	websitetext = getWebpage("http://www.dictionary.com")
	indexstart = websitetext.find("wotdAudio-play")
	wordoftheday = websitetext[websitetext.find(">", indexstart) + 1: websitetext.find("<", indexstart)]
	return wordoftheday

#this function will grab the definition of the word based on the url
def getdef(word):
	websitedef = getWebpage("http://www.dictionary.com/browse/" + word)
	indexstart = websitedef.find('name="description"')
	startofdef = websitedef.find("content=", indexstart) + 9
	definition = websitedef[startofdef: websitedef.find('.', startofdef) + 1]
	return definition

wotd = getWotd()
print "The word of the day is: " + wotd.capitalize() + "\n" + getdef(wotd)
