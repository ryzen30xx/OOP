from monster import Monster

class AirMonster(Monster):
  def __init__(self, strength: int, health: int, height: int):
    super().__init__(strength, health)
    self.__height = height

  @property
  def height(self) -> int:
    return self.__height

  @height.setter
  def height(self, value: int):
    self.__height = value

  def move(self, x: int, y: int):
    print(f"Move to ({x}, {y}) position with fly above {self.__height} kilometers in the air")
    self._Monster__position = (x, y)

  def attack(self):
    print(f"Attack enemy with {self.strength} damage from the sky")

# air_monster = AirMonster(strength=40, health=160, height=15)
# air_monster.move(5, 15)
# air_monster.attack()
