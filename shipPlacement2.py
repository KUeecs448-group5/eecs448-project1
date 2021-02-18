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


#call to place all ships for one player
def placeShip(player, shipCount):
  #player 1 = 0, player 2 = 1
  for i in range(1, shipCount+1): #i = size of ship curently placing
    print('Placing Size ' + str(i) + ' Ship')
    orient = input('Horizontal or Vertical?(H/V): ')#code for verifing valid h or v for orientation
    while not((orient == 'H') or (orient == 'V') or (orient == 'h') or (orient == 'vhh')):
      orient = input('Invalid Character Please Enter "H" or "V": ')
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
