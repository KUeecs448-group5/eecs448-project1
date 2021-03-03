#Name: Caden Kroonenberg

import Print, shotDetection, shipPlacement2
from termcolor import colored

userInput = "0";

print("Please give the number of people that will be playing.");
print();

while userInput != "1" and userInput != "2":
    userInput = input("Type '1' if you want to play against the computer, or '2' if you want to play against another person.");
    print();
    if (userInput != "1" and userInput != "2"):
        print("Invalid input. Please try again");
        print();

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

run(shipCount)

if userInput == "1":
    # call AI code
    print("AI");
elif userInput == "2":
    # call two-player code
    print("2-player");
