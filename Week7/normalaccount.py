from account import Account

class NormalAccount(Account):
	def __init__(self, id, name):
		super().__init__(id, name);

	def widthdraw(self, amount):
		if amount <= 0:
			print('Amount must be greater than 0');

		if amount > self.balance:
			print('Insufficient balance');
			return
		self._balance -= amount
		print(f'Widthdrawal successful. Current balance: {self.balance}');


	def __Str__(self):
		return super().__str__() + ", Type: Normal Account"