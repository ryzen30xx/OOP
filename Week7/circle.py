from shape import Shape

class Circle(Shape):
	def __init__(self, name, radius):
		super().__init__(name);
		self.__radius = radius;
		self._type = 'Circle';

	@property
	def radius(self):
		return self.__radius;

	@radius.setter
	def radius(self, value):
		self.__radius = value;

	#override the abstract method from parent class
	def area(self):
		return 3.14 * self.__radius ** 2;