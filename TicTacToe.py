board=["-","-","-","-","-","-","-","-","-"]
print " Player 1 is X and Player 2 is O.\n Pretend the board is like a telephone\n and the numbers correspond to the spots on the board.\n"
winner=False
player1Turn=True
player2Turn=False


def isWinner(board,letter,spot):
    if spot%2!=0:
     if (board[0]==letter and board[4]==letter and board[8]==letter) or (board[2]==letter and board[4]==letter and board[6]==letter):
         return True
    #2 above
    if spot > 6 and board[spot-4]==letter and board[spot-7]==letter:
        return True
    #2 below
    if spot < 4 and board[spot+2]==letter and board[spot+5]==letter:
        return True 
    #1 above 1 below
    if spot > 3 and spot < 7 and board[spot-4]==letter and board[spot+2]==letter:
        return True
    #2 right
    if spot%3==1 and board[spot]==letter and board[spot+1]==letter:
        return True
    #2 left
    if spot%3==0 and board[spot-2]==letter and board[spot-3]==letter:
        return True
    #1 right 1 left
    if spot%3==2 and board[spot-2]==letter and board[spot]==letter:
        return True
    return False

while winner==False:
        if player1Turn==True:
            spot=input("Player 1 enter a spot number.\n")
        else:
            spot=input("Player 2 enter a spot number.\n")
        if spot <1 or spot>9 or board[spot-1]!= "-":
            while spot <1 or spot>9 or board[spot-1]!= "-":
                spot=input("Invalid spot. Pick another spot.\n")
        
        if player1Turn==True:
            board[spot-1]="X"
            player1Turn=False
            player2Turn=True
            winner=isWinner(board,"X",spot);
        else:
            board[spot-1]="O"
            player2Turn=False
            player1Turn=True
            winner=isWinner(board,"O",spot)
        print board[0:3]
        print board[3:6]
        print board[6:9]
        if winner == True:
            print "Game Over!"
            if player1Turn==False:
                print "Player 1 Wins!"
            else:
                print "Player 2 Wins!"
        




