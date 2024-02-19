class Cat:
	def __init__(self, name, owner):
		self.name = name
		self.owner = owner

	def say(self):
		print(f'{self.name} say meow !')
		print('dit me Hong Hoang')

tom = Cat('Tommy', 'John')
Keera = Cat('Kerra', 'John')

class Owner:
	def __init__(self, name: str, pet):
		self.name = name
		self.pet = pet

	def show_pet(self):
		print(f"I'm {self.name} and my pet is {self.pet.name}")

print(tom.name, tom.owner)
print(Keera.name, Keera.owner)

# tom.say()
# Keera.say()
John = Owner('John', tom)
John.show_pet()
# tom.name = 'Tom'
# Keera.name = 'Panda'

# tom.say()
# Keera.say()

