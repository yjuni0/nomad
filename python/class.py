class Dog:

  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed  

class GuardDog(Dog): #부모 클래스에서 inherit 받기  blabla(top class) 

  def __init__(self, name, breed):
    super().__init__(
      name=name,
      age=5,
      breed=breed
    )
    self.spoiled = True # 상속받은 method 외에 각자의 method 갖을 수 있음
  def rrrrr(self):
    print("stay away!")

class Puppy(Dog):

  def __init__(self, name, breed):
    super().__init__(
      name=name,
      age=0.1,
      breed=breed
    )
    self.aggressive = True

  # def __str__(self):
  #   return f"{self.breed} puppy named {self.name} {self.age} years"

  def woof_woof(self):
    print("Woof Woof!")

  # def introduce(self):
  #   print(f"My name is {self.name} and I am a little {self.breed}")
  #   self.woof_woof()

ruffus = Puppy(
  name="Ruffus",
  breed="Beagle", 
)
bibi = GuardDog(
  name="Bibi",
  breed="Dalmatian",
)

print(ruffus.aggressive)

bibi.rrrrr()


