#Name: Caden Kroonenberg
#user shot selection

import shipPlacement

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
    if player == 1:
        shotArr = p1shotArr
        enemyShipArr = shipPlacement.p2shipArr
    else:
        shotArr = p2shotArr
        enemyShipArr = shipPlacement.p1shipArr
    
    #shot selection
    repeat = True
    while repeat == True:
        repeat = False
        xChar = input('Enter a column [A-J] to fire upon: ')
        print("xChar:", xChar)
        if xChar == "A" or xChar == "a":
            xCoord = 0
        elif xChar == "B" or xChar == "b":
            xCoord = 1
        elif xChar == "C" or xChar == "c":
            xCoord = 2
        elif xChar == "D" or xChar == "d":
            xCoord = 3
        elif xChar == "E" or xChar == "e":
            xCoord = 4
        elif xChar == "F" or xChar == "f":
            xCoord = 5
        elif xChar == "G" or xChar == "g":
            xCoord = 6
        elif xChar == "H" or xChar == "h":
            xCoord = 7
        elif xChar == "I" or xChar == "i":
            xCoord = 8
        elif xChar == "J" or xChar == "j":
            xCoord = 9
        else:
            print("Invalid input. Try again")
            repeat = True
    yCoord = int(input('Enter a row [1-10] to fire upon: '))
    yCoord = yCoord - 1

    #register shot
    shotArr[yCoord][xCoord] = 1

    #shot feedback
    if enemyShipArr[yCoord][xCoord] == shotArr[yCoord][xCoord]:
        print("Shot hit!")
    else:
        print("Shot missed.")
