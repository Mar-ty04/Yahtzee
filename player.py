from die import Die

class Player:
  def __init__(self):
    self._dice = [Die(), Die(), Die()]
    self._dice.sort()
    self._points = 0

  def get_points(self):
    return self._points

  def roll_dice(self):
    for die in self._dice:
      die.roll()
    self._dice.sort()

  def has_pair(self):
    if self._dice[0]._value == self._dice[1]._value or self._dice[1]._value == self._dice[2]._value or self._dice[0]._value == self._dice[2]._value:
      self._points += 1
      return True
      
    else:
      return False
      
  def has_three_of_a_kind(self):
    if self._dice[0]._value == self._dice[1]._value == self._dice[2]._value:
      self._points += 3
      return True
      
    else:
      return False

  def has_series(self):
    if self._dice[2]._value - self._dice[1]._value == 1 and self._dice[1]._value - self._dice[0]._value == 1:
      self._points += 2
      return True
      
    else:
      return False

  def __str__(self):
    return f"D1={self._dice[0]._value}, D2={self._dice[1]._value}, D3={self._dice[2]._value}"