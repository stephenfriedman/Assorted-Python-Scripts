import webbrowser

#webbrowser.open("http://reddit.com")

def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return ""


depth=input("How many pages deep would you like to go?")
webpage=input("What webpage would you like to start with?")
keyword=input("What keyword would you like to track?")
page= get_page("http://www.batw.net/htmllessons/example_page.html")
dict={};
for word in page.split():
    if dict.has_key(word):
        dict[word]=dict[word]+1;
    else:
        dict[word]=1;


if dict.has_key(keyword):	    
        print "Your keyword " + '"'+ keyword +'"'+ " appears " + str(dict[keyword]) + " times"
else:
        print "Your keyword does not appear on the page."
