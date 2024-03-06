class Bank:
	def __init__(self, name):
		self.__name = name;
		self.__accounts = [];

	def add(self, acc):
		self.__accounts.append(acc);

	def withdraw(self, id, amount):
		acc = self.__find_account(id);
		if not acc:
			return f'Account with ID {id} not found'

		acc.withdraw(amount);

	def __find_account(self, id):
		for acc in self.__accounts:
			if acc.id == id:
				return acc;

		return None;

	def show_account(self, id):
		acc = self.__find_account(id);
		if not acc:
			print(f'account with ID {id} not found');

		print(acc);