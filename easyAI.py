import random

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

validPos = False

boardEmpty = True
unHit = 100

while boardEmpty:
    xCoor = random.randint(0, 9)
    yCoor = random.randint(0, 9)
    print(xCoor)
    print(yCoor)
    print()
    if shotArrAI[xCoor][yCoor] == 0:
        shotArrAI[xCoor][yCoor] = 1
        unHit = unHit - 1

    if unHit == 0:
        boardEmpty = False

print(shotArrAI)

