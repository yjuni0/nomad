"""
def tax_calc(money):
  return money*0.35
def pay_tax(tax):
  print("thank you for paying",tax)

to_pay = tax_calc(15000000)
pay_tax(to_pay)
"""

"""
my_name="yejun"
my_age = 29
my_color_eyes = "darkbrown"

print(f"Hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color")
"""

"""
def make_juice(fruit):
  return f"{fruit}+🥤"
def add_ice(jucie):
  return f"{jucie}+🧊"
def add_sugar(iced_juice):
  return f"{iced_juice}+🍬"

jucie = make_juice("🍎")
cold_juice = add_ice(jucie)
perfect_jucie = add_sugar(cold_juice)
print(perfect_jucie)
"""

"""
def main(winner):
  if winner < 100:
    print("If")
  else:
    print("false")

print(main(102))
"""

"""

from random import randint

print("Welcome to Python casino")
pc_choice  = randint(1, 50)

playing = True
attempts = 5

while playing:
  user_choice = int(input("Choose number:"))
  attempts -= 1
  if user_choice == pc_choice:
    print("You win!")
    playing = False
  elif attempts == 0:
    print(f"Game over! The correct number was {pc_choice}.")
  elif user_choice > pc_choice:
    print("Lower!")
  else:
    print("Higher!")
"""

# days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
# print(days_of_week[0])
