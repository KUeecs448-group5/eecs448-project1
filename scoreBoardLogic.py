#Name: Nick Velicer
#an interface that stores the initial player or ai arrays and updates the score based on the player array after each shot


startingArray1 = [[]]
startingArray2 = [[]]
initialShipNumber1 = 0
initialShipNumber2 = 0

#fills a local variable with the initial placements for the players/ai
def initializeScore(arr1, arr2):
    global startingArray1
    global startingArray2
    global initialShipNumber1
    global initialShipNumber2
    startingArray1 = arr1
    startingArray2 = arr2
    initialShipNumber1 = spotsRemaining(startingArray1)
    initialShipNumber2 = spotsRemaining(startingArray2)


#takes in an initialized 10x10 2d array
def spotsRemaining(array):
    shipSpots = 0
    for i in range(10):
        for j in range(10):
            if array[i][j] != 0:
                shipSpots += 1
    return shipSpots


#takes in updated player/ai arrays, returns [score1, score2]
def returnScores(current1, current2):
    shotDiff1 = initialShipNumber1 - spotsRemaining(current1)
    shotDiff2 = initialShipNumber2 - spotsRemaining(current2)
    return [shotDiff1, shotDiff2]


#prints a command line representation of each player's score based on their current board states
def printScoreboard(array1, array2, aiCheck):
    print('')
    print('        Scores:       ')
    print('----------------------')
    if aiCheck:
        print('Player: ', returnScores(array1, array2)[0], "/", initialShipNumber1)
        print('AI: ', returnScores(array1, array2)[1], "/", initialShipNumber2)
    else:
        print('Player 1: ', returnScores(array1, array2)[0], "/", initialShipNumber1)
        print('Player 2: ', returnScores(array1, array2)[1], "/", initialShipNumber2)
    print('----------------------')
    print('')




