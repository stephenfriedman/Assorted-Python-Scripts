#Stephen Friedman
#The Best Love Letters ever created by a Billy Bob
#This program creates a basic love letter. It accomplishes
##this by selecting random words out of a text document I
##compiled. This document is a giant list of words compiled from
##other love letters, lists of raomantic words, poems, and more.
##I decided against trying to create formal sentence sturcture
##since I found that I was not able to make varying sentences,
##and that each sentence would look almost the same as the last.
##Even with using a few different types of sentence structures,
##the letters looked very robotic and awkward. I resorted back
##to the random option that I used here, since it makes many of
##the sentences sound very poetic, artsy, and high level writing.
##This lab was a blast to do, and should definitely be implemented
##into the curriculum for future ATCS classes.

def getLoveLetter():
    import random
    #Get my text file
    myFile=open('loveletteropenings.txt','r')
    openingWords=myFile.read()
    randOpeningWord=random.choice(openingWords.split())
    myFile1=open('randomStuff.txt','r')
    loveWords=myFile1.read()
    #Delete unnecessary characters from text
    loveWords.replace(":"," ");
    loveWords.replace('"'," ");
    loveWords.replace(';'," ");
    loveWords.replace('('," ");
    loveWords.replace(')'," ");

    #Create a title for the letter
    output="."
    output=output+ '"'+random.choice(loveWords.split()).upper()+'"\n'
    output=output+" \n\n"
    #Create a letter opening
    output=output+ "My "+randOpeningWord+",\n\n"
    output=output+" "
    counter=-1
    #Writes 10 lines in the letter
    for num in range(0,10):
        output=output+"\n"
        #Set sentence size between 4 and 8 words
        randNum=random.randrange(4,8)
        first=random.choice(loveWords.split()).lower()
        firstLetter=first[0]
        rest=first[1:len(first)]
        #Capitalize first letter in each sentence
        first=firstLetter.upper()+rest
        output=output+ first+" "
        #Makes rest of the words in the sentence
        for sentence in range(0,randNum):
          output=output+random.choice(loveWords.split()).lower()
          output=output+" "
          sentence=sentence+1
        output=output+ ".\n"
        num=num+1
    output=output+" \n"
    output=output+" \n"
    endings=open('endings.txt','r')
    endWords=endings.read()
    #Create a ranom ending
    endWord=random.choice(endWords.split("/"))
    output=output+ endWord+", \n"
    output=output+" \n"
    output=output+ "Billy Bob"
    return output


print getLoveLetter()
