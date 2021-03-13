#Name: Caden Kroonenberg

import Print, shotDetection, shipPlacement2, aiPlacement, aiShotDetection, scoreBoardLogic
from termcolor import colored

def run(shipCount):
    """
    implements every method of battleship game and checks for winner every turn
    shipCount: number of ships(potentially of various sizes) that each player has.
    Precondition: player variable initialized.
    Postcondition: checks win condition every turn and declares winner when one player has no ships remaining.
    """
    endGame = False
    player = 1

    print()
    print("Player 1:")
    print()
    shipPlacement2.placeShip(0, shipCount)
    player = 2
    input("Press Enter and then switch players to continue...")
    print(chr(27) + "[2J")
    print("Player 2:")
    print()
    shipPlacement2.placeShip(1, shipCount)
    player = 1
    input("Press Enter and then switch players to continue...")
    print(chr(27) + "[2J")
    scoreBoardLogic.initializeScore(shipPlacement2.playArr[0], shipPlacement2.playArr[1])

    while not endGame:
        if player == 1:
            print("Player 1:")
        elif player == 2:
            print("Player 2:")
        Print.printTopMap(player)
        print()
        Print.printBottomMap(player)
        shotDetection.shot(player)

        #check win condition and switch players if not
        if player == 1:
            if shotDetection.p1shotCount >= winCount:
                endGame = True
                print("\nPlayer 1 Wins!\n")
            else:
                player = 2
                print(chr(27) + "[2J")
        elif player == 2:
            if shotDetection.p2shotCount == winCount:
                endGame = True
                print("\nPlayer 2 Wins!\n")
            else:
                player = 1
                print(chr(27) + "[2J")

def runAI(shipCount):
    """
    implements every method of battleship game and checks for winner every turn
    shipCount: number of ships(potentially of various sizes) that each player has.
    Precondition: player variable initialized.
    Postcondition: checks win condition every turn and declares winner when one player has no ships remaining.
    """
    endGame = False
    player = 1

    print()
    print("Player 1:")
    print()
    shipPlacement2.placeShip(0, shipCount)
    player = 2
    input("Press Enter and then switch players to continue...")
    print(chr(27) + "[2J")
    print("Player 2:")
    print()
    aiPlacement.placeShip(1, shipCount)
    player = 1
    input("Press Enter and then switch players to continue...")
    print(chr(27) + "[2J")
    scoreBoardLogic.initializeScore(shipPlacement2.playArr[0], shipPlacement2.playArr[1])

    while not endGame:
        if player == 1:
            print("Player 1:")
        elif player == 2:
            print("Player 2:")
        Print.printTopMap(player)
        print()
        Print.printBottomMap(player)
        # shotDetection.shot(player) original
        aiShotDetection.shot(player)
        #check win condition and switch players if not
        if player == 1:
            if aiShotDetection.p1shotCount >= winCount: # original shotDetection.p1shotCount >= winCount:
                endGame = True
                print("\nPlayer 1 Wins!\n")
            else:
                player = 2
                print(chr(27) + "[2J")
        elif player == 2:
            if aiShotDetection.p2shotCount == winCount: # original shotDetection.p2shotCount == winCount:
                endGame = True
                print("\nPlayer 2 Wins!\n")
            else:
                player = 1
                print(chr(27) + "[2J")

print(chr(27) + "[2J")
print(colored("BATTLESHIP", 'blue', 'on_grey'))
print()

repeat = True
while repeat == True:
        repeat = False
        shipCount = input("Enter ship count [1-6]: ")
        if not shipCount.isnumeric():
            print("Invalid input (not an integer). Try again")
            repeat = True
        elif int(shipCount) > 6 or int(shipCount) < 1:
            print("Invalid input. Try again")
            repeat = True
        winCount = 0
        for i in range(1,int(shipCount)+1):
          winCount = winCount + i

userInput = input("If you would like to play against the computer type 'computer', otherwise type any characters for a two-player game ")

if (userInput == "computer"):
    level = input("Please choose a difficulty level: Type 'Easy', 'Medium', or 'Hard' ")

    if (level == "Medium"):
        aiShotDetection.ai = 1
    elif (level == "Hard"):
        aiShotDetection.ai = 2
    # default is easy level
    else:
        aiShotDetection.ai = 0

if userInput == "computer":
    runAI(shipCount)
else:
    run(shipCount)
