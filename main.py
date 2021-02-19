#Name: Caden Kroonenberg

import shotDetection, shipPlacement2

#print top map - 'X' denotes successful shot, 'O' denotes missed shot, '^' denotes area not fired upon
def printTopMap(player):
    if player == 1:
        enemyShipArr = shipPlacement2.p2shipArr
        shotArr = shotDetection.p1shotArr
    elif player == 2:
        enemyShipArr = shipPlacement2.p1shipArr
        shotArr = shotDetection.p2shotArr
    print("  A B C D E F G H I J")
    for i in range(0, 10):
        if(i < 9):
            print("", i+1, end="")
        else:
            print(i+1, end="")
        for j in range(0, 10):
            if shotArr[i][j] == 0:
                print("^", end =" ")
            elif shotArr[i][j] == 1 and enemyShipArr[i][j] == 0:
                print("O", end =" ")
            elif shotArr[i][j] == 1 and enemyShipArr[i][j] == 1:
                print("X", end =" ")
            #elif statement for sunk ship - #; requires isSunk() function and ship object
        print()

#print bottom map - 'X' denotes ship placement, '*' denotes hit ship, '^' denotes area not fired upon by enemy
def printBottomMap(player):
    if player == 1:
        shipArr = shipPlacement2.p1shipArr
        shotArr = shotDetection.p2shotArr
    elif player == 2:
        shipArr = shipPlacement2.p2shipArr
        shotArr = shotDetection.p1shotArr
    print("  A B C D E F G H I J")
    for i in range(0, 10):
        if(i < 9):
            print("", i+1, end="")
        else:
            print(i+1, end="")
        for j in range(0, 10):
            if shipArr[i][j] == 0:
                print("^", end =" ")
            elif shotArr[i][j] == 1 and shipArr[i][j] == 1:
                print("*", end =" ")
            elif shotArr[i][j] == 0 and shipArr[i][j] == 1:
                print("X", end =" ")
            #elif statement for sunk ship - #; requires isSunk() function and ship object
        print()

def run(shipCount):
    endGame = False
    player = 1
    
    print("Player 1:")
    shipPlacement2.placeShip(player, shipCount)
    player = 2
    print("Player 2:")
    shipPlacement2.placeShip(player, shipCount)
    player = 1

    while not endGame:
        if player == 1:
            print("Player 1:")
        elif player == 2:
            print("Player 2:")
        printTopMap(player)
        print()
        printBottomMap(player)
        shotDetection.shot(player)
    
        #check win condition and switch players if not
        if player == 1:
            if shotDetection.p1shotArr == shipPlacement2.p2shipArr:
                endGame = True
                print("\nPlayer 1 Wins!\n")
            else:
                player = 2
                print(chr(27) + "[2J")
        elif player == 2:
            if shotDetection.p2shotArr == shipPlacement2.p1shipArr:
                endGame = True
                print("\nPlayer 2 Wins!\n")
            else:
                player = 1
                print(chr(27) + "[2J")

print("\nBATTLESHIP\n")

repeat = True
while repeat == True:
        repeat = False
        shipCount = int(input("Enter ship count [1-5]: "))
        if shipCount > 5 or shipCount < 1:
            print("Invalid input. Try again")
            repeat = True

run(shipCount)