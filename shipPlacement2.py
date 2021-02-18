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

#declairing the coordinate variables outside of a definition so they have a larger scope.
xCoord = 0
yCoord = 0
face = 0

#made userInput function, so it can easily be called again in the event of a misplaced ship
def userInput(i):
    print('Placing Size ' + str(i) + ' Ship')
    orient = input('Horizontal or Vertical?(H/V): ')#code for verifing valid h or v for orientation
    while not((orient == 'H') or (orient == 'V') or (orient == 'h') or (orient == 'v')):
      orient = input('Invalid Character Please Enter "H" or "V": ')
    if orient == "H" or orient == "h":#convert orient into a number, 0 is horizontal, 1 is vertical
      face = 0
    elif xChar == "V" or xChar == "v":
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


#call to place all ships for one player
def placeShip(player, shipCount):
  #player 1 = 0, player 2 = 1
  for i in range(1, shipCount+1): #i = size of ship curently placing
    userInput(i)#fetch orientation and coordinates
    print(face)
