import random

class Die:
  def __init__(self, sides = 6):
    self._sides = sides
    self._value = self.roll()

  def roll(self):
    self._value = random.randint(1, self._sides)
    return self._value 

  def __str__(self):
    return str(self._value)

  def __lt__(self, other):
    return self._value < other._value
    
  def __eq__(self, other):
    return self._value == other._value

  def __sub__(self, other):
    return (self._value - other._value)