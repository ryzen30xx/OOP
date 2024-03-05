from animal import Animal
class Pet(Animal):
	def __init__(self,name, age, owner):
		super().__init__(name, age);
		self.__owner = owner;

	@property
	def owner(self):
		return self._owner
	@owner.setter
	def owner(self, value):
		self.__owner = value;

	