#Marisol Morales & Andreas Moreno, 2/28/24, Lab 5 Yahtzee

import check_input
from player import Player

def take_turn(player):
  player.roll_dice()
  print(str(player))
  
  if player.has_three_of_a_kind():
    print("You got 3 of a kind!")
    
  elif player.has_series():
    print("You got a series of 3!")
    
  elif player.has_pair():
    print("You got a pair!")
    
  else:
    print("Aww. Too Bad.")
    
  print(f"Score = {player.get_points()}")

def main():
  print('-Yahtzee-')
  print()
  player_1 = Player()
  play_again = True
  while play_again is True:
    take_turn(player_1)
    play_again = check_input.get_yes_no('Play again? (Y/N): ')
    print()
    if play_again is False:
      print('Game Over.')
      print(f'Final score = {player_1.get_points()}')
      break
  
main()