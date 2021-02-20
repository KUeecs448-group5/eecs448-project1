#ship class
class Ship:
  #ship constructor used s1 = Ship(size, player(bool))  
  def __init__(self, size, player):
    self.size = size
    self.health = size
    self.player = player


        
  #called everytime the ship is hit
  def hit(self):
    """
    If called, determines ship health and determines whether or not ship is sunk
    self: referring to itself 
    Precondition:Ship object initialized.
    Postcondition:Called Ship object's health reduced, or Ship object declared sunk. 
    """
    self.health = self.health - 1
    if self.health == 0:
      if self.player == 0:
        print("Player 1 sunk Player 2's size", self.size, "ship")
      if self.player == 1:
        print("Player 2 sunk Player 1's size", self.size, "ship")
