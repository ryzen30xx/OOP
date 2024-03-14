from bank import Bank
from account import Account
from normalaccount import NormalAccount
from debit_account import DebitAccount

class BankProgram:
	def __init(self):
		self.__bank = Bank('MeMayBank');

	def run(self):
		self.__print_menu();

		choice = input('Your Choice: ');
		if 	 choice == 1: self.__add_account()
		elif choice == 2: self.__widthdraw()
		elif choice == 3: self.__deposit()
		elif choice == 4:  self.__show_account()
		elif choice == 5: break
		else:print ("invalid choice");	 