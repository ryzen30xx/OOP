




#000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


class Company:
	def __init__(self, name, employee):
		self.__name = name
		self.__employee = []

	def add_emp(self,)

class Employee:
	def __init__(self, name, salary, years):
		self.__name = name;
		self.__salary = salary;
		self.__years = years;

	def get_salary(self):
		return(self.__salary);

	def set_salary(self, salary):
		if salary < 0:
			raise ValueError('Enter wrong number!');
		else:
			self.__salary = salary;

	def set_name(self, name):
		if name == "":
			print("Name must be have one letter!");
		else:
			self.__name = name;

	def show(self):
		return(f'Name: {self.__name}, Salary: ${self.__salary}, Year of experience: {self.__years}');
