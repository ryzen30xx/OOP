from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self,id,name):
        self.__id = id
        self.__name = name
        self._balance = 0

    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def balance(self):
        return self._balance
    @abstractmethod
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        if amount <= 0: 
            print('amount must be greater than 0')
            return
        self._balance += amount
        print(f'deposit successful. Current balance: {self.balance}')

    def __str__(self):
        return f'ID : {self.id}, Name : {self.name}, Balance : {self.balance}'


acc01 = Account(1,'Lu')
acc01.deposit(248)
acc01.show()
acc01.withdraw(163)
acc01.show()