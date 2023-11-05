import random

class Auto:
    def __init__(self, brand):
        self.brand = brand
    def behavior(self, act):
        self.act = act
        return f"Car: {self.act}"
ran = ''
car1 = Auto("Toyota")
car2 = Auto("Honda")
car3 = Auto("Ford")
car4 = Auto("Chevrolet")
car5 = Auto("BMW")
def randomazer(car):
  global ran
  name = ''
  if car == 1:
    name = 'Toyota'
  elif car == 2:
    name = 'Honda'
  elif car == 3:
    name = 'Ford'
  elif car == 4:
    name = 'Chevrolet'
  elif car == 5:
    name = 'BMW'
  ranget = random.randint(1,3)
  if ranget == 1:
    ran = "You stopped your " + name + " near park"
  elif ranget == 2:
    ran = "You drove your " + name + " to lake"
  elif ranget == 3:
    ran = "You drove your "+ name +" to mechanic"
  else:
    ran = "You stayed at home"
randomazer(car = 1)
print(car1.behavior(ran))
randomazer(car = 2)
print(car2.behavior(ran))
randomazer(car = 3)
print(car3.behavior(ran))
randomazer(car = 4)
print(car4.behavior(ran))
randomazer(car = 5)
print(car5.behavior(ran))
