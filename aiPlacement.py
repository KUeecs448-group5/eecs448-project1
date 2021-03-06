# Name: Nick Velicer
#modifying original shipPlacement2.py code from Jiacheng Chen and Wesley Sportsman


from shipObject import Ship
import random, Print, shipPlacement2

AIshipArr = [
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


# userInput to be called repeatedly in case of a bad ship placement
def userInput(i):
    """
    Randomly returns a ship placement to be tested at the according ship size
    i: current size of the ship being placed
    Precondition: player variable initialized
    Postcondition: potential ship coordinates are returned
    """
    random.seed(None)
    face = random.randint(0, 1)
    xCoord = random.randint(0, 9)
    yCoord = random.randint(0, 9)
    return xCoord, yCoord, face


def shipDefiner(x, y, z, t):  # looks at the request space, if available places ship and returns true, otherwise returns false
    # x,y,z,t = xCoord, yCoord, orientation, size
    # first check if ship is hanging off end
    """
    Helper method to placeShip, makes sure placeShip is in valid area.
    x:xCoord
    y:yCoord
    z:orientation(vertical or horizontal)
    t: size(size of ship)
    Precondition: Ship object initialized
    Postcondition: Ship object is in valid position or is rejected
    """
    if z == 0:  # check horizontal hang off
        if (x + t - 1) > 9:
            return False
    if z == 1:  # check vertical hang off
        if (y + t - 1) > 9:
            return False
    if AIshipArr[y][x] != 0:  # check if first node is occupied
        return False
    if z == 0:  # check horizontal occupied
        for i in range(1, t):  # should run from 1 to t-1
            if AIshipArr[y][x + i] != 0:
                return False
        for i in range(0, t):  # if it runs this for loop, the ship is in a valid position and the array can be changed
            AIshipArr[y][x + i] = t  # using t as a unique marker for each ship
    if z == 1:  # same thing for vertical
        for i in range(1, t):  # should run from 1 to t-1
            if AIshipArr[y + i][x] != 0:
                return False
        for i in range(0, t):
            AIshipArr[y + i][x] = t
    return True


objArr = []


# call to place all ships for the AI
def placeShip(shipCount):
    """
    places Ship object on board with shipDefiner and userInput methods.
    shipCount: number of ships(potentially of various sizes) that each player has.
    Precondition: player variable initialized, shipCount value from 1-6
    Postcondition: ship object is placed on board
    """
    # player 1 = 0, player 2 = 1, AI = 2
    for i in range(1, int(shipCount) + 1):  # i = size of ship currently placing
        input = userInput(i)  # fetch orientation and coordinates
        xVar, yVar, fVar = input
        test = shipDefiner(xVar, yVar, fVar, i)
        while test == False:  # run it again if placement failed
            input = userInput(i)
            xVar, yVar, fVar = input
            test = shipDefiner(xVar, yVar, fVar, i)
        objArr.append(Ship(i, 2))


#a simple console test to see the randomly generated board
'''
placeShip(5)
for i in range(10):
    print(AIshipArr[i])
'''
