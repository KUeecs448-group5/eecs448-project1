import shotDetection

#print top map - 'X' denotes successful shot, 'O' denotes missed shot, '^' denotes area not fired upon
def printTopMap(player):
    if player == 1:
        enemyShipArr = p2shipArr
        shotArr = shotDetection.p1shotArr
    elif player == 2:
        enemyShipArr = p1shipArr
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
        shipArr = p1shipArr
        shotArr = shotDetection.p2shotArr
    elif player == 2:
        shipArr = p2shipArr
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
    endGame = 0
    player = 1
    #shipPlacement for shipCount amount of ships

    while not endGame:
        if player == 1:
            print("Player 1:")
        elif player == 2:
            print("Player 2:")
        printTopMap(player)
        print()
        printBottomMap(player)
        shotDetection.shot(player)
        if player == 1:
            player = 2
        elif player == 2:
            player = 1
        #check for win condition
        #clear screen and tell players to switch

p1shipArr = [
             [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
             [0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 
             [0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]

p2shipArr = [
             [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
             [0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 
             [0, 1, 0, 0, 0, 0, 0, 1, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]

shipCount = 5

run(shipCount)