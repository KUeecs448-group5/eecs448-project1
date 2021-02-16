#Name: Jiacheng Chen

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

import main
 
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
    for shipBodyPart in range(1, shipCount +1):
        print('Place the #' + str(shipBodyPart) + 'of' + str(shipCount) + 'of the ship')
        xCoord = int(input('Enter a X coordinate of the new ship to place: '))
        yCoord = int(input('Enter a Y coordinate of the new ship to place: '))
        parts.append((xCoord, yCoord))
    parts = canonicalizeParts(parts)
    if not isAdjacent(parts):
            raise Exception()
    if player:
        #Player 1
        if overlaps(parts, p1shipArr):
            raise Exception()
        placeBody(parts,p1shipArr)
    else:
        #Player 2
        if overlaps(parts, p1shipArr):
            raise Exception()
        placeBody(parts, p2shipArr)