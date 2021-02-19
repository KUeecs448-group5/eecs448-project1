# eecs448-project1

This project brings the Battleship board game to the terminal through a simple Python program. Each player's shots and ships are tracked in 2D bool arrays.

To begin the game, each player will place their ships in a 10x10 grid.
Players will then take turns firing upon eachother's ships, without knowing where there targets are.
While taking a "turn" players will see two boards:
  The top board displays the shots the current player has taken at their enemy as well as the outcome of those shots (hit or miss)
  The bottom board displays the current player's ships as well as their status - how many times (if any) they've been hit by the enemy
This process will repeat until a player wins by sinking all of their opponent's ships.
