# KayLee Mitchell
# Medium AI control

import random, easy, aiShotDetection, shipPlacement2

shotArrAI = [
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

next_shot = 0
"""
    0 => next shot is a random shot
    1 => next shot is looking up
    2 => next shot is looking right
    3 => next shot is looking down
    4 => next shot is looking left
"""

orientation = 2
"""
    0 => vertical
    1 => horizontal
    2 => unknown
"""

x_orig = 0
y_orig = 0
"""
    coordinate of initial hit of a ship
"""

x_ref = 0
y_ref = 0
"""
    coordinate from which we are looking, not always the initial hit
"""

hit = False
"""
    keeps track of if the shot was a hit or a miss
"""

"""
    generates a random shot
    records if its a hit or miss

    if its a hit, record the initial location (x, y)
    then iterate through next available spaces going clockwise starting up

    the only case not included is the 1x1 ship case that gets hit
        this will be taken care of outside the code

"""
playerShipArr = shipPlacement2.p1shipArr

def simpleAIShooter(xCoord, yCoord):
    global next_shot
    next_shot = 1

    if (next_shot == 1):
        upHit = simpleLookUp(xCoord, yCoord)

    return upHit

def simpleLookUp(x, y):
    global x_ref, y_ref
    x_ref = x
    y_ref = y - 1

    if (playerShipArr[y_ref][x_ref] != 0 and shotArrAI[y_ref][x_ref] == 0):
        shotArrAI[y_ref][x_ref] = 1
        return "Hit"
    else:
        return "Miss"
