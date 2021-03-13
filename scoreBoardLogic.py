#Name: Nick Velicer
#an interface that stores the initial player or ai arrays and updates the score based on the player array after each shot


startingArray1 = [[]]
startingArray2 = [[]]


#fills a local variable with the initial placements for the players/ai
def initializeScore(arr1, arr2):
    startingArray1 = arr1
    startingArray2 = arr2


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
    shotDiff1 = spotsRemaining(current1)
    shotDiff2 = spotsRemaining(current2)
    return [shotDiff1, shotDiff2]




