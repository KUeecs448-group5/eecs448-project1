#Name: Caden Kroonenberg

shipArr = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
shotArr = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def shot():
    xCoord = int(input('Enter a X coordinate: '))
    yCoord = int(input('Enter a Y coordinate: '))
    shotArr[xCoord][yCoord] = 1
    
    #print map
    for i in range(0, 9):
        for j in range(0, 9):
            if shotArr[i][j] == 0:
                print("^", end='')
            elif shotArr[i][j] == 1: # and shipArr[i][j] == 0:
                print("O", end='')
            elif shotArr[i][j] == 1: # and shipArr[i][j] == 1:
                print("X", end='')
        print()

    #shot detection
    if shipArr[xCoord][yCoord] == shotArr[xCoord][yCoord]:
        print("Shot hit!")
    else:
        print("Shot missed.")


if shipArr[0][0] == 1: bool
{
    print("please jesus")
}

shot()