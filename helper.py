myFile=open('c:/pyth/randomStuff.txt','r')
words=myFile.read()
words=words.replace("'"," ")
words=words.replace(","," ")
print words
