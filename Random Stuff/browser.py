#Stephen Friedman
import webbrowser
import urllib

#Get user input for depth setting, search query, and starting site 
userWord=input("What word would you like to track?(Please put in quotes)")
userDepth=input("What depth would you like to search to?")
userLink=input("What link would you like to start with? (Please put it in quotes)")


#Get all the source code of a web page
def get_page(url):
	try:
		return urllib.urlopen(url).read()
	except:
		return ""
#Set page = user's starting site	
page=get_page(userLink)
#List that will hold every link that was read through
links=[]

#Gets every link
def allLinks(i,url):
        while i > 0:
                currLinks=getPageLinks(url)
                for link in currLinks:
                        links.append(link)
                        allLinks(i-1,link)
                i=0
                


def getPageLinks(url):
        linkList=[]
        pageText=get_page(url)
        for word in page.split('href="'):
               aLink=""
               end=word.find('"')
               aLink=aLink+word[0:end]
               if aLink.startswith("http://www."):
                       if not aLink.endswith(".css") or aLink.endswith(".ico") :
                               linkList.append(aLink)
        return linkList

def occurences(word,link):
        return get_page(link).count(word)

linkDict={}                    
def rank(word):
        printList=[]
        for link in links:
               times = occurences(word,link)
               linkDict[link]=times
               printList.append(times)
        printList.sort()
        for number in printList:
                for linkName in linkDict.keys():
                        if linkDict[linkName]==number:
                               print linkName
                               print linkDict[linkName]
                               del linkDict[linkName]
                               break
                        
allLinks(userDepth,userLink)
rank(userWord)
