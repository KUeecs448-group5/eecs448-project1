import shipPlacement2, shotDetection, aiPlacement, aiShotDetection
from termcolor import colored

#print top map - 'X' denotes successful shot, 'O' denotes missed shot, '^' denotes area not fired upon

def printTopMap(player):
    """
    Prints target mapping of turn player(coordinates that turn player has shot, and that denotes whether hit and missed enemy, and locations
    has not shot at yet)
    player: tells program whose turn it is
    Precondition: player variable initialized
    Postcondition: target mapping of turn player printed in command line
    """
    if player == 1:
        enemyShipArr = shipPlacement2.p2shipArr
        shotArr = shotDetection.p1shotArr # original shotDetection.p1shotArr
    elif player == 2:
        enemyShipArr = shipPlacement2.p1shipArr
        shotArr = shotDetection.p2shotArr # original shotDetection.p2shotArr
    print("Shots taken at enemy:")
    print("  A B C D E F G H I J")
    for i in range(0, 10):
        if(i < 9):
            print("", i+1, end="")
        else:
            print(i+1, end="")
        for j in range(0, 10):
            if shotArr[i][j] == 0:
                print(colored("^ ", 'blue'), end ='')
            elif shotArr[i][j] == 1 and enemyShipArr[i][j] == 0:
                print(colored("O ", 'white', 'on_white'), end ='')
            elif shotArr[i][j] == 1 and not enemyShipArr[i][j] == 0:
                print(colored("X ", 'red', 'on_red'), end ='')
            #elif statement for sunk ship - #; requires isSunk() function and ship object
        print()

#print bottom map - 'X' denotes ship placement, '*' denotes hit ship, '^' denotes area not fired upon by enemy
def printBottomMap(player):
    """
    Prints out map of turn player's ship placements
    player: tells program whose turn it is
    Precondition: player variable initialized
    Postcondition: turn player's ship placements printed in command line
    """
    if player == 1:
        shipArr = shipPlacement2.p1shipArr
        shotArr = shotDetection.p2shotArr
    elif player == 2:
        shipArr = shipPlacement2.p2shipArr
        shotArr = shotDetection.p1shotArr

    print("Your ships:")
    print("  A B C D E F G H I J")
    for i in range(0, 10):
        if(i < 9):
            print("", i+1, end="")
        else:
            print(i+1, end="")
        for j in range(0, 10):
            if shipArr[i][j] == 0:
                print(colored("^ ", 'blue'), end ="")
            elif shotArr[i][j] == 1 and not shipArr[i][j] == 0:
                print(colored("* ", 'red', 'on_grey'), end ="")
            elif shotArr[i][j] == 0 and not shipArr[i][j] == 0:
                print(colored("* ", 'white', 'on_grey'), end ="")
            #elif statement for sunk ship - #; requires isSunk() function and ship object
        print()
