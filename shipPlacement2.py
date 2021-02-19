#Name: Jiacheng Chen
#Name: Wesley Sportsman
p1shipArr = [
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

p2shipArr = [
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
playArr = [p1shipArr,p2shipArr]


#made userInput function, so it can easily be called again in the event of a misplaced ship
def userInput(i):
    print('Placing Size ' + str(i) + ' Ship')
    orient = input('Horizontal or Vertical?(H/V): ')#code for verifing valid h or v for orientation
    while not((orient == 'H') or (orient == 'V') or (orient == 'h') or (orient == 'v')):
      orient = input('Invalid Character Please Enter "H" or "V": ')
    if orient == "H" or orient == "h":#convert orient into a number, 0 is horizontal, 1 is vertical
      face = 0
    elif orient == "V" or orient == "v":
      face = 1
    print("Please give the leftmost/topmost node of your ship")
    xChar = input('Which column [A-J]?: ') #code for x coordinate
    repeat = True
    while repeat == True:
      repeat = False
      if xChar == "A" or xChar == "a":
        xCoord = 0
      elif xChar == "B" or xChar == "b":
        xCoord = 1
      elif xChar == "C" or xChar == "c":
        xCoord = 2
      elif xChar == "D" or xChar == "d":
        xCoord = 3
      elif xChar == "E" or xChar == "e":
        xCoord = 4
      elif xChar == "F" or xChar == "f":
        xCoord = 5
      elif xChar == "G" or xChar == "g":
        xCoord = 6
      elif xChar == "H" or xChar == "h":
        xCoord = 7
      elif xChar == "I" or xChar == "i":
        xCoord = 8
      elif xChar == "J" or xChar == "j":
        xCoord = 9
      else:
        xChar = input('Invalid input. Please enter a valid column [A-J]: ')
        repeat = True
    yChar = input('Which Row [1-10]?: ') #user input for y
    repeat = True
    while repeat == True:
      if not yChar.isnumeric(): #make sure it is a number
        yChar = input('Invalid input. Please enter a valid row [1-10]: ')
      elif not ((int(yChar) > 0) and (int(yChar) < 11)):#verification
        yChar = input('Invalid input. Please enter a valid row [1-10]: ')
      else:
        repeat = False
    yCoord = int(yChar) - 1 #change to 0-9
    return xCoord,yCoord,face

def shipDefiner(x,y,z,t,p):#looks at the request space, if avalible places ship and returns true, otherwisr returns falce
#x,y,z,t,p = xCoord, yCoord, orientation, size, player
#first check if ship is hanging off end
  if z == 0: #check horizontal hang off
    if (x + t - 1) > 9:
      return False
  if z == 1: #check vertical hang off
    if (y + t - 1) > 9:
      return False
  if playArr[p][y][x] != 0: #check if first node is occupied
    return False
  if z == 0: #check horizontal occupied
    for i in range(1,t): #should run from 1 to t-1
      if playArr[p][y][x+i] != 0:
        return False
    for i in range(0,t): #if it runs this for loop, the ship is in a valid position and the array can be changed
      playArr[p][y][x+i] = t #using t as a unique marker for each ship
  if z == 1: #same thing for vertical
    for i in range(1,t): #should run from 1 to t-1
      if playArr[p][y+i][x] != 0:
        return False
    for i in range(0,t):
      playArr[p][y+i][x] = t 
  return True    

#call to place all ships for one player
def placeShip(player, shipCount):
  #player 1 = 0, player 2 = 1
  for i in range(1, shipCount+1): #i = size of ship curently placing
    input = userInput(i)#fetch orientation and coordinates
    xVar,yVar,fVar = input
    test = shipDefiner(xVar,yVar,fVar,i,player)
    while test == False: #run it again if placement failed 
      print('Your Ship failed to be placed, please verify you are placing your ship in a valid location. Restarting the process.')
      input = userInput(i)
      xVar,yVar,fVar = input
      test = shipDefiner(xVar,yVar,fVar,i,player)
