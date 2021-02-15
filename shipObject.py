#ship class
class Ship:
  #ship constructor used s1 = Ship(size, player(bool))  
  def __init__(self, size, player):
    self.size = size
    self.health = size
    self.player = player

  #called when ship is sunk
  def sunk(self):
    if self.player == 0:
        # message to executive
        #print("Player 2 Wins")
    if self.player == 1:
        # message to executive
        #print("Player 1 Wins")
        
  #called everytime the ship is hit
  def hit(self):
    self.health = self.health - 1
    if self.health == 0:
      self.sunk()
