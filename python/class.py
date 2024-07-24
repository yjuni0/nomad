
class Puppy:

  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed

  def __str__(self):
    return f"{self.breed} puppy named {self.name} {self.age} years"

  def woof_woof(self):
    print("Woof Woof!")

  def introduce(self):
    print(f"My name is {self.name} and I am a little {self.breed}")
    self.woof_woof()

ruffus = Puppy(
  name="Ruffus",
  breed="Beagle",
  age=0.3
)
bibi = Puppy(
  name="Bibi",
  breed="Dalmatian",
  age=0.1
)


ruffus.introduce()

bibi.introduce()


