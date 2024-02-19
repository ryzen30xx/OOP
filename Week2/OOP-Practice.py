class Employee:
	def __init__(self, name, salary, year, pet):
		self.name = name
		self.salary = int(salary)
		self.year = int(year)
		self.pet = pet


	def show(self):
		print(f'{self.name}, {self.salary:,.2f}, {self.year}')

	def show_pet(self):
		print(f'My name is {self.name} and my pet have a name is {self.pet}')

Hau = Employee('Pham Duc Hau', 20000, 2004, 'Tommy')

Hau.show()

Hau.show_pet()