import webbrowser

def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return ""



page= get_page("http://www.batw.net/htmllessons/example_page.html")
dict={};
for word in page.split('href='):
    if dict.has_key(word):
        dict[word]=dict[word]+1;
    else:
        dict[word]=1;


cat="blahhhthebannndds"
print cat.split("the")

        
