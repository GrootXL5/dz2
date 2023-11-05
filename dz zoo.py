class Zoo:
  total_animals = 0
  total_zoos = 0

  def __init__(self, animal_type, can_fly=False, can_swim=False, can_walk=True):
      self.animal_type = animal_type
      self.can_fly = can_fly
      self.can_swim = can_swim
      self.can_walk = can_walk
      Zoo.total_animals += 1

  def fly(self):
      if self.can_fly:
          return f"{self.animal_type} flew"
      else:
          return f"This {self.animal_type} cannot fly"

  def swim(self):
      if self.can_swim:
          return f"{self.animal_type} swam"
      else:
          return f"This {self.animal_type} cannot swim"

  def walk(self):
      if self.can_walk:
          return f"{self.animal_type} walked"
      else:
          return f"This {self.animal_type} cannot walk"
tiger = Zoo("Tiger")
bird = Zoo("Bird", can_fly=True, can_swim=False)
dolphin = Zoo("Dolphin", can_fly=False, can_swim=True)
snake = Zoo("Snake", can_fly=False, can_swim=False, can_walk=True)
print(tiger.fly())
print(bird.fly())
print(dolphin.fly())
print(snake.fly())
print(tiger.swim())
print(bird.swim())
print(dolphin.swim())
print(snake.swim())
print(tiger.walk())
print(bird.walk())
print(dolphin.walk())
print(snake.walk())
print(Zoo.total_animals)