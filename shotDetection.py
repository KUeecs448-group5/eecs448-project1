#Name: Caden Kroonenberg

shipArr = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
shotArr = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#user shot selection
def shot():
    xCoord = int(input('Enter a X coordinate: '))
    yCoord = int(input('Enter a Y coordinate: '))
    shotArr[xCoord][yCoord] = 1

    #shot feedback
    if shipArr[xCoord][yCoord] == shotArr[xCoord][yCoord]:
        print("Shot hit!")
    else:
        print("Shot missed.")
 
#Will place a single ship in shipArr. Will throw runtime error if ship doesnt fit in array or overlaps w/ another ship.
def placeShip():
    print("placeShip() func")
    #code

#print top map - 'X' denotes successful shot, 'O' denotes missed shot, '^' denotes area not fired upon
def printTopMap():
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
def printBottomMap():
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

shot()
printTopMap()
print("----------")
printBottomMap()