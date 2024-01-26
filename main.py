
import random

gameOver = False
player1Score = 0
player2Score = 0

winner = 1

def printCurrentScores():
    print("Player 1 Score => "+ str(player1Score))
    print("Player 2 Score => "+ str(player2Score))

def checkForGameOver():
    global winner
    global player1Score
    global player2Score
    global gameOver

    if player1Score > 100:
        gameOver = True
        winner = 1
    if player2Score > 100:
        gameOver = True
        winner = 2

def handleGameOver():
    print("Winner is player " + str(winner))

def getChoice(player):
    if player == 1:
        print("Press 1 to bank or 2 to roll =>")
        choice = input()
    else:
        aiChoice = random.randint(1,2)
        if aiChoice == 1:
            choice = "1"
        else:
            choice = "2"

    return choice

def doTurn(player):
    global player1Score
    global player2Score

    roundDone = False
    roundScore = 0
    while not roundDone:
        
        roll = random.randint(1,6)
        print("Rolled a "+str(roll))
        if roll >= 2:
            roundScore= roundScore+ roll
        else:
            roundDone= True
        
        print("Round score  "+str(roundScore))
        printCurrentScores()
        if not roundDone:
            choice = getChoice(player)

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
                roundDone = False


while not gameOver:
    checkForGameOver()

    print("====================================================")
    print("Player 1 - it's your turn")
    if not gameOver:
        doTurn(1)
    else:
        handleGameOver()

    checkForGameOver()

    print("====================================================")
    print("Player AI - it's your turn")
    if not gameOver:
        doTurn(2)
    else:
        handleGameOver()

