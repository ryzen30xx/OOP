class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self):
        return self.__numerator
    
    @numerator.setter
    def numerator(self, value):
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator
    
    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ValueError('Denominator cannot be zero')
        self.__denominator = value
    
    def add(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def sub(self, other):
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def mul(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def div(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        if denominator == 0:
            raise ValueError('Division by zero')
        return Fraction(numerator, denominator)
    
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'


class DemoFraction:
    def __init__(self, numerator, denominator):
        self.__fraction1 = Fraction(numerator, denominator)
        self.__fraction2 = Fraction(numerator, denominator)

    def enter_fraction1(self, numerator, denominator):
        self.__fraction1.numerator = numerator
        self.__fraction1.denominator = denominator

    def enter_fraction2(self, numerator, denominator):
        self.__fraction2.numerator = numerator
        self.__fraction2.denominator = denominator

    def add(self, fraction1, fraction2):
        return fraction1.add(fraction2)
    
    def sub(self, fraction1, fraction2):
        return fraction1.sub(fraction2)
    
    def mul(self, fraction1, fraction2):
        return fraction1.mul(fraction2)
    
    def div(self, fraction1, fraction2):
        return fraction1.div(fraction2)
    
    def run(self):
        print(f'Fraction 1: {self.__fraction1}')
        print(f'Fraction 2: {self.__fraction2}')
        print(f'Add: {self.add(self.__fraction1, self.__fraction2)}')
        print(f'Sub: {self.sub(self.__fraction1, self.__fraction2)}')
        print(f'Mul: {self.mul(self.__fraction1, self.__fraction2)}')
        print(f'Div: {self.div(self.__fraction1, self.__fraction2)}')

    def print_menu(self):
        print('1. Enter fraction 1')
        print('2. Enter fraction 2')
        print('3. Add')
        print('4. Subtract')
        print('5. Multiply')
        print('6. Divide')
        print('7. Exit')
        return
    
    def run_menu(self):
        while True:
            self.print_menu()
            choice = int(input('Enter choice: '))
            if choice == 1:
                numerator = int(input('Enter numerator: '))
                denominator = int(input('Enter denominator: '))
                self.enter_fraction1(numerator, denominator)
            elif choice == 2:
                numerator = int(input('Enter numerator: '))
                denominator = int(input('Enter denominator: '))
                self.enter_fraction2(numerator, denominator)
            elif choice == 3:
                print(f'Add: {self.add(self.__fraction1, self.__fraction2)}')
            elif choice == 4:
                print(f'Sub: {self.sub(self.__fraction1, self.__fraction2)}')
            elif choice == 5:
                print(f'Mul: {self.mul(self.__fraction1, self.__fraction2)}')
            elif choice == 6:
                print(f'Div: {self.div(self.__fraction1, self.__fraction2)}')
            elif choice == 7:
                break
            else:
                print('Invalid choice')
        return
    
if __name__ == '__main__':
    program = DemoFraction(1, 1)
    program.run_menu()
    program.run()