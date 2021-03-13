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
        upCoords = simpleLookUp(xCoord, yCoord)
        print("up coordinates")



def AIshooter(xCoord, yCoord):
    global next_shot, orientation, x_orig, y_orig, x_ref, y_ref, hit

    hit = True
    x_orig = xCoord
    y_orig = yCoord

    next_shot = 1
    orientation = 2
    # x_orig = shot[0]
    # y_orig = shot[1]
    x_ref = x_orig
    y_ref = y_orig

    if next_shot == 1:
        look_up(x_ref, y_ref)
    elif next_shot == 2:
        look_right(x_ref, y_ref)
    elif next_shot == 3:
        look_down(x_ref, y_ref)
    elif next_shot == 4:
        look_left(x_ref, y_ref)
    # else:
    #     # random shot, record x and y coordinate in tuple shot
    #     if hit:
    #         next_shot = 1
    #         orientation = 2
    #         # x_orig = shot[0]
    #         # y_orig = shot[1]
    #         x_ref = x_orig
    #         y_ref = y_orig
    #     else:
    #         next_shot = 0
    #         orientation = 2
    #         x_orig = 0
    #         y_orig = 0
    #         x_ref = x_orig
    #         y_ref = y_orig

    return [x_ref, y_ref];

def look_up(x,y):
    global next_shot, orientation, x_orig, y_orig, x_ref, y_ref, hit

    # shoot at the position (x, y-1)
    if not hit and orientation != 0:
        # the next direction is right >
        next_shot = 2
        x_ref = x_orig
        y_ref = y_orig
    elif not hit and orientation == 0:
        # the next direction is down >
        next_shot = 3
        x_ref = x_orig
        y_ref = y_orig
    # hit!
    else:
        # look up again >
        next_shot = 1
        orientation = 0
        x_ref = x
        y_ref = y - 1




    return [x_ref, y_ref]

def look_right(x,y):
    global next_shot, orientation, x_orig, y_orig, x_ref, y_ref, hit

    # shoot at position (x+1, y)
    if not hit and orientation != 1:
        # the next direction is down >
        next_shot = 3
        x_ref = x_orig
        y_ref = y_orig
    elif not hit and orientation == 1:
        # the next direction is left >
        next_shot = 4
        x_ref = x_orig
        y_ref = y_orig
    # hit!
    else:
        # look right again >
        next_shot = 2
        orientation = 1
        x_ref = x + 1
        y_ref = y

    return

def look_down(x,y):
    global next_shot, orientation, x_orig, y_orig, x_ref, y_ref, hit

    # shoot at position (x, y+1)
    if not hit and orientation != 0:
        # the next direction is left >
        next_shot = 4
        orientation = 1
        x_ref = x_orig
        y_ref = y_orig
    elif not hit and orientation == 0:
        # ship is sunk!
        next_shot = 0
        orientation = 2
        x_orig = 0
        y_orig = 0
        x_ref = x_orig
        y_ref = y_orig
    else:
        # look down again >
        next_shot = 3
        orientation = 0
        x_ref = x
        y_ref = y + 1

    return

def look_left(x,y):
    global next_shot, orientation, x_orig, y_orig, x_ref, y_ref, hit

    # shoot at position (x-1, y)
    if not hit:
        # a ship has been sunk!
        next_shot = 0
        orientation = 2
        x_orig = 0
        y_orig = 0
        x_ref = x_orig
        y_ref = y_orig
    # hit!
    else:
        # look left again >
        next_shot = 4
        orientation = 1
        x_ref = x - 1
        y_ref = y

    return
