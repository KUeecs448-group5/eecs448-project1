import shotDetection

p1shipArr = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
p1shotArr = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
p2shipArr = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
p2shotArr = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#play(5)

#print top map - 'X' denotes successful shot, 'O' denotes missed shot, '^' denotes area not fired upon
def printTopMap(player: bool):
    if(player):
        shipArr = p1shipArr
        shotArr = p1shotArr
    else:
        shipArr = p2shipArr
        shotArr = p2shotArr
    for i in range(0, 9):
        for j in range(0, 9):
            if shotArr[i][j] == 0:
                print("^", end='')
            elif shotArr[i][j] == 1 and shipArr[i][j] == 0:
                print("O", end='')
            elif shotArr[i][j] == 1 and shipArr[i][j] == 1:
                print("X", end='')
            #elif statement for sunk ship - #; requires isSunk() function and ship object
        print()

#print bottom map - 'X' denotes ship placement, '*' denotes hit ship, '^' denotes area not fired upon by enemy
def printBottomMap(player: bool):
    if(player):
        shipArr = p1shipArr
        shotArr = p1shotArr
    else:
        shipArr = p2shipArr
        shotArr = p2shotArr
    for i in range(0, 9):
        for j in range(0, 9):
            if shipArr[i][j] == 0:
                print("^", end='')
            elif shotArr[i][j] == 1 and shipArr[i][j] == 1:
                print("*", end='')
            elif shotArr[i][j] == 0 and shipArr[i][j] == 1:
                print("X", end='')
            #elif statement for sunk ship - #; requires isSunk() function and ship object
        print()

def play(shipCount: int):
    endGame = 0
    player = 1
    #shipPlacement for shipCount amount of ships

    while not endGame:
        if player:
            print("Player 1:")
        else:
            print("Player 2:")
        printTopMap(player)
        printBottomMap(player)
        shotDetection.shot(player)
        player = not player
        #check for win condition
        #clear screen and tell players to switch