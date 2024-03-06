from account import Account

class DebitAccount(Account):
	def __init__(self, id, name, limit):
		super().__init__(id, name);
		def widthdraw(self, amount):

		if amount > self.balance + self.__limit:
			print('Insufficient balance');
			return;

		if amount <= 0:
			print('Amount must be greater than 0');
			return;

		
		self._balance -= amount
		print(f'Widthdrawal successful. Current balance: {self.balance}');


	def __Str__(self):
		return super().__str__() + ", Type: Debit Account, Limit: -$" + self.__limit