class LightBulb:
	def __init__(self, name):
		self.__name = name;
		self.__light = False;


	@property
	def name(self):
		return self.__name;

	@name.setter
	def name(self, value):
		self.__name = value;

	def turn_on(self):
		self.__light = True;

	def turn_off(self):
		self.__light = False;

	def show(self):
		print(f"{self.__name} is {'on' if self.__light else 'off'}");


class LightColor:
	def __init__(self, name, color):
		self.__name = name;
		self.__color = color;

	@property
	def color(self, value):
		self.__color = value;


class MultiLightColor:
	
	