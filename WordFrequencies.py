#myFile=open('c:/pyth/warandpeace.txt','r')
#text=myFile.read();
words="This is certainly an interesting move for the Wild. Rupp does not play an altogether different game than Powe, though Rupp has much more size, and is certainly not afraid to drop the gloves. This has to be a move to improve the size of the team. The Wild have been pushed around this season, and adding Rupp to the lineup, along with Coyle, puts two big bodies in the line up in a short amount of time."
dict={};
for word in words.split():
    if dict.has_key(word):
        dict[word]=dict[word]+1;
    else:
        dict[word]=1;

seed=input("Seed length: ")


print dict;
