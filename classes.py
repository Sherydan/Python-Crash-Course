import math

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    @staticmethod
    def obtenerPy():
        return math.pi
    
    def greetings(self):
        return f'My name is {self.name} and i am {self.age}'
    def hasBirthday(self):
        self.age += 1

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance

    def greetings(self):
        return f'My name is {self.name} and i am {self.age} and my balance is {self.balance} '


luis = User('Luis tobar', 'luchito@gmail.com', 27)
luis.hasBirthday()

juan = Customer('juanito baeza', 'juanito@gmai.com', 24)
juan.setBalance(400)

print(User.obtenerPy())