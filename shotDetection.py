#Name: Caden Kroonenberg
import main
#user shot selection
def shot(player):
    if player == 1:
        shotArr = main.p1shotArr
        shipArr = main.p2shipArr
    else:
        shotArr = main.p2shotArr
        shipArr = main.p1shipArr
    xCoord = int(input('Enter a X coordinate to fire upon: '))
    yCoord = int(input('Enter a Y coordinate to fire upon: '))
    shotArr[xCoord][yCoord] = 1

    #shot feedback
    if shipArr[xCoord][yCoord] == shotArr[xCoord][yCoord]:
        print("Shot hit!")
    else:
        print("Shot missed.")
