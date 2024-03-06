from abc import ABC, abstractmethod

#to define an abstract class, let it 
class Shape(ABC):
	def __init__(self, name):
		self._name = name; # protected method
		self._type = 'Shape'; # protected method

	@property
	def name(self):
		return self._name;
	
	@name.setter
	def name(self, value):
		self._name = value;

	@property
	def type(self):
		return self._type;
	
	@abstractmethod
	def area(self):
		pass;

	# override the __str__ method from the parent class
	def __str__(self):
		return f'{self.type} {self.name}'