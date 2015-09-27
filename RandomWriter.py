import random
myFile=open('c:/pyth/warandpeace.txt','r')
words=myFile.read();
words=words.upper();
seed=input("Input Desired Seed Length: ")
randStart=random.randrange(0,len(words)-seed)
seedString=words[randStart:randStart+seed]#get a random starting point in the text
while(len(seedString)<150):
    #This creates a list with each entry beginning with the first char after
    #the seed sequence. This sequence is increased 1 char each time in this loop.
    list=words.split(seedString[len(seedString)-seed:len(seedString)])         
    afterSeq=""#this variable will contain all the first chars after the last n
    #letters in the seed from inside the text
    for seq in list:
       if seq[0]=="":#if the first char after a seed occurrence is a space
           afterSeq=afterSeq+" "
       else:#if the fisrt char after a seed occurrence is not a space
            afterSeq=afterSeq+seq[0]
    
    #add to the seed 1 random char from afterSeq, which is the vairable that
    #represents all the first chars after the seed inside the text        
    seedString=seedString+afterSeq[random.randrange(0,len(afterSeq))]
    
print seedString
