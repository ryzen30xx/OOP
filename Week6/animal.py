class Animal:
	def __init__(self, name, age):
		self.__name = name;
		self.__age = age;

	@property
	def name(self):
		return self.__name;

	@name.setter
	def name(self, value):
		self.__name = value;

	@property
	def age(self):
		return self.__age;

	@age.setter
	def age(self, value):
		self.__age = value;
		
	
	def show(self):
		print(f"Dog name {self.__name}\n age: {self.__age}");


