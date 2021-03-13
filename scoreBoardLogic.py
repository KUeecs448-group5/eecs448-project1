#Name: Nick Velicer
#an interface that stores the initial player or ai arrays and updates the score based on the player array after each shot


startingArray1 = [[]]
startingArray2 = [[]]
initialShipNumber1 = 0
initialShipNumber2 = 0
scores = [0, 0]

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


#prints a command line representation of each player's score based on their current board states
def printScoreboard(aiCheck):
    print('')
    print('        Scores:       ')
    print('----------------------')
    if aiCheck:
        print('Player: ', scores[0], "/", initialShipNumber1)
        print('AI: ', scores[1], "/", initialShipNumber2)
    else:
        print('Player 1: ', scores[0], "/", initialShipNumber1)
        print('Player 2: ', scores[1], "/", initialShipNumber2)
    print('----------------------')




