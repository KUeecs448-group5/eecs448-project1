# KayLee Mitchell
# Medium AI control

import random, easy, aiShotDetection, shipPlacement2, shotDetection

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

shotArr = shotDetection.p2shotArr

next_shot = 1
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
    # pseudocode
    # 1. set next_shot variable
    global next_shot
    # if (next_shot == 0):
    #     next_shot = 1
    result = "Miss"
    if (aiShotDetection.aiCoordinatesHitAt[0] != 10 and next_shot == 0):
        next_shot = 1
    # 2. write conditional for next_shot
    # 3. in conditional, check for appropriate position for hit
        # 1. if hit
        # 2. is miss
    if next_shot != 0:
        # corresponds to looking up
        if next_shot == 1:
            result = simpleLookUp(xCoord, yCoord)
            if result != "Hit":
                next_shot = 2
            else:
                next_shot = 0
                aiShotDetection.aiCoordinatesHitAt = [10, 10]

        elif next_shot == 2:
            result = simpleLookRight(xCoord, yCoord)
            if result != "Hit":
                next_shot = 3
            else:
                next_shot = 0
                aiShotDetection.aiCoordinatesHitAt = [10, 10]

        elif next_shot == 3:
            result = simpleLookDown(xCoord, yCoord)
            if result != "Hit":
                next_shot = 4
            else:
                next_shot = 0
                aiShotDetection.aiCoordinatesHitAt = [10, 10]

        elif next_shot == 4:
            result = simpleLookLeft(xCoord, yCoord)
            next_shot = 0
            aiShotDetection.aiCoordinatesHitAt = [10, 10]
    else:
        aiShotDetection.aiCoordinatesHitAt = [10, 10]
        next_shot = 1

    return [x_ref, y_ref]


def simpleLookUp(x, y):
    global x_ref, y_ref
    if (y > 0):
        x_ref = x
        y_ref = y - 1
        if (shotArr[y_ref][x_ref] == 0):
            print("result of simpleLookUp", y_ref, x_ref)
            if (playerShipArr[y_ref][x_ref] != 0 and shotArrAI[y_ref][x_ref] == 0):
                shotArrAI[y_ref][x_ref] = 1
                return "Hit"
            else:
                return "Miss"
        else:
            x_ref = x
            y_ref = y
            simpleLookRight(x_ref, y_ref)
    else:
        x_ref = x
        y_ref = y
        simpleLookRight(x_ref, y_ref)

def simpleLookDown(x, y):
    global x_ref, y_ref

    if (y < 9):
        x_ref = x
        y_ref = y + 1
        if (shotArr[y_ref][x_ref] == 0):
            print("result of simpleLookDown", y_ref, x_ref)
            if (playerShipArr[y_ref][x_ref] != 0 and shotArrAI[y_ref][x_ref] == 0):
                shotArrAI[y_ref][x_ref] = 1
                return "Hit"
            else:
                return "Miss"
        else:
           x_ref = x
           y_ref = y
           simpleLookLeft(x_ref, y_ref)
    else:
        x_ref = x
        y_ref = y
        simpleLookLeft(x_ref, y_ref)


def simpleLookRight(x, y):
    global x_ref, y_ref

    if (x < 9):
        x_ref = x + 1
        y_ref = y
        if (shotArr[y_ref][x_ref] == 0):
            print("result of simpleLookRight", y_ref, x_ref)
            if (playerShipArr[y_ref][x_ref] != 0 and shotArrAI[y_ref][x_ref] == 0):
                shotArrAI[y_ref][x_ref] = 1
                return "Hit"
            else:
                return "Miss"
        else:
           x_ref = x
           y_ref = y
           simpleLookDown(x_ref, y_ref)
    else:
        x_ref = x
        y_ref = y
        simpleLookDown(x_ref, y_ref)

def simpleLookLeft(x, y):
    global x_ref, y_ref

    if (x > 0):
        x_ref = x - 1
        y_ref = y
        if (shotArr[y_ref][x_ref] == 0):
            print("result of simpleLookLeft", y_ref, x_ref)
            if (playerShipArr[y_ref][x_ref] != 0 and shotArrAI[y_ref][x_ref] == 0):
                shotArrAI[y_ref][x_ref] = 1
                return "Hit"
            else:
                return "Miss"
        else:
           x_ref = x
           y_ref = y
    else:
        x_ref = x
        y_ref = y
