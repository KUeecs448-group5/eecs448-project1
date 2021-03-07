# Name: Caden Kroonenberg and Michael Cooley
# user shot selection


import easy, shipPlacement2, time ,hardAI, shotDetection

p1shotCount = 0
p2shotCount = 0

p1shotArr = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

p2shotArr = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def shot(player):
    """
    Allows Player to shoot, depending on which player
    player: tells method which player is shooting currently
    Precondition: player variable to be initialized
    Postcondition: depending on which player, one value of opposing player is changed
    """
    if player == 1:
        shotArr = shotDetection.p1shotArr # original p1shotArr
        enemyShipArr = shipPlacement2.p2shipArr
    else:
        shotArr = shotDetection.p2shotArr # original p2shotArr
        enemyShipArr = shipPlacement2.p1shipArr

    # shot selection
    repeatAll = True
    while repeatAll == True:
        repeat = True
        while repeat == True:
            repeat = False
            if player == 1:
                xChar = input('Enter a column [A-J] to fire upon: ')
            else:
                ai = 2
                if( ai == 0):
                    xShot = easy.getShot()
                    xChar = xShot[0]
                #elif( ai == 1):
                   # xShot = medium.getShot()
                   # xChar = xShot[0]
                elif (ai == 2):
                    xShot = hardAI.hitShip()
                    xChar = xShot[0]
            if xChar == "A" or xChar == "a" or xChar == 0:
                xCoord = 0
            elif xChar == "B" or xChar == "b" or xChar == 1:
                xCoord = 1
            elif xChar == "C" or xChar == "c" or xChar == 2:
                xCoord = 2
            elif xChar == "D" or xChar == "d" or xChar == 3:
                xCoord = 3
            elif xChar == "E" or xChar == "e" or xChar == 4:
                xCoord = 4
            elif xChar == "F" or xChar == "f" or xChar == 5:
                xCoord = 5
            elif xChar == "G" or xChar == "g" or xChar == 6:
                xCoord = 6
            elif xChar == "H" or xChar == "h" or xChar == 7:
                xCoord = 7
            elif xChar == "I" or xChar == "i" or xChar == 8:
                xCoord = 8
            elif xChar == "J" or xChar == "j" or xChar == 9:
                xCoord = 9
            else:
                print("Invalid input. Try again")
                repeat = True

        repeat = True
        while repeat == True:
            repeat = False
            if player == 1:
                yCoord = input('Enter a row [1-10] to fire upon: ')
                if int(yCoord) > 10 or int(yCoord) < 1:
                    print("Invalid input (out of [1-10] range). Try again")
                    repeat = True
                elif not yCoord.isnumeric():
                    print("Invalid input (not an integer). Try again")
                yCoord = int(yCoord) - 1
            else:
                yCoord = (xShot[1])

        repeatAll = False
        if shotArr[yCoord][xCoord] == 1:
            print("You have already fired on this location, please select another space:")
            repeatAll = True

    # register shot
    shotArr[yCoord][xCoord] = 1

    # shot feedback
    if not enemyShipArr[yCoord][xCoord] == 0 and not shotArr[yCoord][xCoord] == 0:
        print(chr(27) + "[2J")
        if player == 1:
            print("Player 1: ", end="")
            global p1shotCount
            p1shotCount = p1shotCount + 1
        elif player == 2:
            global p2shotCount
            p2shotCount = p2shotCount + 1
            print("Player 2: ", end="")
        print("Shot hit!")
        shipPlacement2.objArr[player - 1][enemyShipArr[yCoord][xCoord] - 1].hit()  # register hit in ship object
        input("Switch players then press Enter to continue...")
        print(chr(27) + "[2J")
    else:
        print(chr(27) + "[2J")
        if player == 1:
            print("Player 1: ", end="")
        else:
            print("Player 2: ", end="")
        print("Shot missed.")
        input("Switch players then press Enter to continue...")
