from typing import Any


class Human:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"player: {self.name}"
  
  def __getattribute__(self, name):
    print(f"they want to get {name}")
    return "ㅁ"


class Player(Human):
  def __init__(self, name, xp):
    super().__init__(name)
    self.xp = xp


class Fan(Human):
  def __init__(self, name, fav_team):
    super().__init__(name)
    self.fav_team = fav_team

yejun = Human("yejun")
print(yejun.name)