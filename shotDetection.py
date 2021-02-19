#Name: Caden Kroonenberg
#user shot selection

import shipPlacement2, time

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
        enemyShipArr = shipPlacement2.p2shipArr
    else:
        shotArr = p2shotArr
        enemyShipArr = shipPlacement2.p1shipArr
    
    #shot selection
    repeat = True
    while repeat == True:
        repeat = False
        xChar = input('Enter a column [A-J] to fire upon: ')
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

    repeat = True
    while repeat == True:
        repeat = False
        yCoord = int(input('Enter a row [1-10] to fire upon: '))
        yCoord = yCoord - 1
        if yCoord > 9 or yCoord < 0:
            print("Invalid input. Try again")
            repeat = True


    #register shot
    shotArr[yCoord][xCoord] = 1
    
    #shot feedback
    if not enemyShipArr[yCoord][xCoord] == 0 and not shotArr[yCoord][xCoord] == 0:
        print(chr(27) + "[2J")
        if player == 1:
            print("Player 1: ", end="")
        else:
            print("Player 2: ", end="")
        print("Shot hit!")
        shipPlacement2.objArr[player-1][enemyShipArr[yCoord][xCoord] - 1].hit() #register hit in ship object
        time.sleep(2)
            
        print(chr(27) + "[2J")
    else:
        print(chr(27) + "[2J")
        if player == 1:
            print("Player 1: ", end="")
        else:
            print("Player 2: ", end="")
        print("Shot missed.")
        time.sleep(2)
        print(chr(27) + "[2J")
