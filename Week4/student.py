class Student:
	def __init__(self, ids: int, name, gpa):
		self.__id = ids;
		self.__name = name;
		self.__gpa = gpa;

	def get_id(self):
		return(self.__id);

	def get_name(self):
		return(self.__name);

	def get_gpa(self):
		return(self.__gpa);

	def set_gpa(self, gpa: float):
		if gpa <= 0 and gpa > 10:
			return(0);
		self._gpa = gpa;
		return(f'gpa updated successful');

	def show(self):
		return(f'Student name: {self.__name}\nID: {self.__id}\nGPA: {.self._gpa}')

#