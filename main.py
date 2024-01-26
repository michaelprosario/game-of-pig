
import random

gameOver = False
player1Score = 0
player2Score = 0

winner = 1

def printCurrentScores():
    print("Player 1 Score => "+ str(player1Score))
    print("Player 2 Score => "+ str(player2Score))

def checkForGameOver():
    if player1Score > 100:
        gameOver = true
        winner = 1
    if player2Score > 100:
        gameOver = true
        winner = 2

def doTurn(player):
    roundDone = False
    roundScore = 0
    while not roundDone:
        
        roll = random.randint(1,6)
        print("Rolled a  "+str(roll))
        if roll >= 2:
            roundScore= roundScore+ roll
        else:
            roundDone= True
        
        print("Round score  "+str(roundScore))
        printCurrentScores()
        if not roundDone:
            if player == 1:
                print("Press 1 to bank or 2 to roll =>")
                choice = input()
            else:
                aiChoice = random.randint(1,2)
                if aiChoice == 1:
                    choice = "1"
                else:
                    choice = "2"

            roundScore = roundScore + roll
            if choice == "1": ## Bank 
                print(" banking...")
                if player == 1:
                    player1Score = player1Score + roundScore
                else:
                    player2Score = player2Score + roundScore
                roundScore= 0
                roundDone = True
            else:
                print(" rolling....")


while not gameOver:
    checkForGameOver()

    print("====================================================")
    print("Player 1 - it's your turn")
    if not gameOver:
        doTurn(1)

    checkForGameOver()

    print("====================================================")
    print("Player AI - it's your turn")
    if not gameOver:
        doTurn(2)

