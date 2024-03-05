from monster import Monster

class SeaMonster(Monster):
  def __init__(self, strength: int, health: int, depth: int):
    super().__init__(strength, health)
    self.__depth = depth

  @property
  def depth(self) -> int:
    return self.__depth

  @depth.setter
  def depth(self, value: int):
    self.__depth = value

  def move(self, x: int, y: int):
    print(f"Swim to ({x}, {y}) position under {self.__depth} kilometers in the sea")
    self._Monster__position = (x, y)

  def attack(self):
    print(f'Attack enemy {self.strength} damage')


# sea_monster = SeaMonster(strength=25, health=220, depth=7)
# sea_monster.move(5, 10)
# sea_monster.attack()
