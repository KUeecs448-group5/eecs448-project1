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
        shipArr = shipPlacement.p2shipArr
    else:
        shotArr = p2shotArr
        shipArr = shipPlacement.p1shipArr
    
    repeat = True
    while repeat == True:
        repeat = False
        xChar = input('Enter a column [A-J] to fire upon: ')
        if xChar == 'A' or 'a':
            xCoord = 0
        elif xChar == 'B' or 'b':
            xCoord = 1
        elif xChar == 'C' or 'c':
            xCoord = 2
        elif xChar == 'D' or 'd':
            xCoord = 3
        elif xChar == 'E' or 'e':
            xCoord = 4
        elif xChar == 'F' or 'f':
            xCoord = 5
        elif xChar == 'G' or 'g':
            xCoord = 6
        elif xChar == 'H' or 'h':
            xCoord = 7
        elif xChar == 'I' or 'i':
            xCoord = 8
        elif xChar == 'J' or 'j':
            xCoord = 9
        else:
            print("Invalid input. Try again")
            repeat = True
    yCoord = int(input('Enter a row [1-10] to fire upon: ')) - 1
    shotArr[xCoord][yCoord] = 1

    #shot feedback
    if shipArr[xCoord][yCoord] == shotArr[xCoord][yCoord]:
        print("Shot hit!")
    else:
        print("Shot missed.")
