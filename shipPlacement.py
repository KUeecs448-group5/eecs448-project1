#Name: Jiacheng Chen

p1shipArr = [
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

p2shipArr = [
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

def canonicalizeParts(parts):
     parts1 = sorted(parts, key=lambda part: part[0])
     parts2 = sorted(parts1, key=lambda part: part[1])
     return parts2

def isAdjacent(parts):
    keyX = list(set([x[0] for x in parts]))
    keyY = list(set([x[1] for x in parts]))
    if (len(keyX) == 1):
        #In the same row
        if len(keyY) != len(parts):
            return False
        #Adjacent
        if keyY[len(keyY) - 1] - keyY[0] + 1 != len(parts):
            return False
    elif (len(keyY) == 1):
        #In the same col
        if len(keyX) != len(parts):
            return False 
        #Adjacent
        if keyX[len(keyX) - 1] - keyX[0] + 1 != len(parts):
            return False 
    else:
        #Neither in row nor in col
        return False
    return True

def overlaps(parts, shipArr):
    for part in parts:
        x = part[0]
        y = part[1]
        if shipArr[x][y] != 0:
            return True
    return False

def placeBody(parts, shipArr):
    for part in parts:
        x = part[0]
        y = part[1]
        shipArr[x][y] = 1
        
#Will place a single ship in shipArr. Will throw runtime error if ship doesnt fit in array or overlaps w/ another ship.
def placeShip(player, shipCount):
    #player 1 = 1, player 2 = 2
    parts = []

    #one iteration per ship
    for i in range (1, shipCount +1):
        print("Player", player, "Ship", i, ":")
        #one iteration per ship part
        for shipBodyPart in range(1, i+1):
            print('Place part ' + str(shipBodyPart) + ' of ' + str(i) + ' of the [1x' + str(i) + '] ship')
            #A-J and 1-10 notation for consistency
            repeat = True
            while repeat == True:
                repeat = False
                xChar = input('Enter a column [A-J] to place ship: ')
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
            yCoord = int(input('Enter a row [1-10] to place ship: '))
            yCoord = yCoord - 1
            parts.append((xCoord, yCoord))
            print()
        parts = canonicalizeParts(parts)

    #exceptions
    if not isAdjacent(parts):
            raise Exception()
    if player == 1:
        #Player 1
        if overlaps(parts, p1shipArr):
            raise Exception()
        placeBody(parts,p1shipArr)
    else:
        #Player 2
        if overlaps(parts, p2shipArr):
            raise Exception()
        placeBody(parts, p2shipArr)

    #Vertical
    if orientation == "Vertical"
        if xCoord >= 0 and xCood + 2 < len(part)
            if yCoord >= 0 and yCoord < len(part)
                if p1shipArr[xCoord][yCoord] != "1" and p1shipArr[xCoord+1][yCoord] != "1" and p1shipArr[xCoord+2][yCoord] != "1":
                    player 1.part(orientation, xCoord, yCoord,p1shipArr)
                    shipcount = shipcount - 1
                    if shipcount == 0:
                        break
                    else:
                        player 1. show_ship(shipcount, p1shipArr)
                else:
                    print("Enter another Coord: ")
            else:
                print("y coordinate out of bounds, enter y Coord: ")
        else:
            print("x coordinate out of bounds, enter x Coord: ")

    #Horizontal
    if orientation == "Horizontal"
        if xCoord >= 0 and xCood + 2 < len(part)
            if yCoord >= 0 and yCoord < len(part)
                if p1shipArr[xCoord][yCoord] != "1" and p1shipArr[xCoord+1][yCoord] != "1" and p1shipArr[xCoord+2][yCoord] != "1":
                    player 1.part(orientation, xCoord, yCoord,p1shipArr)
                    shipcount = shipcount - 1
                    if shipcount == 0:
                        break
                    else:
                        player 1. show_ship(shipcount, p1shipArr)
                else:
                    print("Enter another Coord: ")
            else:
                print("y coordinate out of bounds, enter y Coord: ")
        else:
            print("x coordinate out of bounds, enter x Coord: ")
            
    #Neither vertical nor horizontal
    if orientation != "Vertical" and orientation == "Horizontal"
        print("Invalid orientation, enter Vertical or Horizontal: ")