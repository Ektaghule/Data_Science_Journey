#OPPS is used for 1)Resuability, 2)Managing Complexity, 3)Extenibility
#Banking system real time case

from abc import abstractmethod
from ast import main
from multiprocessing import managers
from os import name


class Account:
    def __init__(self, account_number, account_holder, balance): #constructor to initialize the account details
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount): #Addint the money to the account
        if amount > 0:
            self.balance += amount 
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
            
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance is {self.balance}")
        else:
            print("Invalid withdrawal amount")
            
    def acc_details(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")
    
#Inheritance: SavingsAccount inherits from Account
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    
#Polymorphism: Account details    
    def acc_details(self):
        print(f"Savings Account Number: {self.account_number}, Balance: {self.balance}, Interest Rate: {self.interest_rate}%")    
    
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest Added: {interest}. New Balance: {self.balance}")
            
#Inheritance: CurrentAccount inherits from Account
class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.balance}")
        else:
            print("Overdraft limit exceeded")
            
#Polymorphism: Overrideint the display method
    def acc_details(self):
        print(f"Current Account: {self.account_number}, Balance: {self.balance}, Overdraft Limit: {self.overdraft_limit}")
        
if __name__=='__main__':
    acc1 = SavingsAccount("SA123","Ekta Ghule", 10000, 3)
    acc2 = SavingsAccount("SA159", "Dilip Mahajaan", 5000, 200)
    
    acc1.deposit(2000)
    acc1.add_interest()
    acc1.acc_details()
    
    acc2.deposit(200)
    acc2.acc_details()
    acc2.withdraw(100)
    
#Encapsulation: Building data and methods that operate though single unit called class
#Task 1: Types of inheritance
#1: Single Inheritance

print("_____Types of Inheritance____")
print("--Single Inheritance--")
class Animal:
    def sound(self):
        print("Animal makes sound")
        
class Dog(Animal):
    pass

d = Dog()
d.sound()

print("Multiple Inheritance")
class Father:
    def money(self):
        print("Father's Money")
        
class Mother:
    def care(self):
        print("Mother's Care")
        
class Child(Father, Mother):
    pass

c = Child()
c.money()
c.care

print("--Multilevel Inheritance--")
class Grandparent:
    def house(self):
        print("Grandparent's House")
        
class Parent(Grandparent):
    pass

class Child(Parent):
    pass

c = Child()
c.house()

print("--Hierarchical Inheritance--")
class Shape:
    def Draw(self):
        print("Drawing a house")
        
class Circle(Shape):
    pass

class Rectangle(Shape):
    pass

Ci = Circle()
R = Rectangle()

Ci.Draw()
R.Draw()

print("--Hybrid Inheritance--")
class A:
    def show(self):
        print("Class A")
        
class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

d = D()
d.show()

#Task 2: Build an e-commerce system where users can browse products, add them to a shopping cart, and check out.

from abc import ABC, abstractmethod

class Product:
    def __init__(self,name, price, stock):
        self.name = name
        self.__price = price
        self.__stock = stock
        
    def get_price(self):
        return self.__price
    
    def reduce_stock(self):
        if self.__stock > 0:
            self.__stock -= 1
    
    def get_discount_price(self):
        return self.__price
    
class Electronics(Product):
    def get_discount_price(self):
        return self.get_price() * 0.90
        
class Clothing(Product):
    def get_discount_price(self):
        return self.get_price() * 0.85
        
class Grocery(Product):
    def get_discount_price(self):
        return self.get_price() * 0.95
        
class Cart(ABC):
    @abstractmethod
    def add(self, product): pass
        
    @abstractmethod
    def remove(self, product): pass
        
    @abstractmethod
    def checkout(self): pass
        
class ShoppingCart(Cart):
    def __init__(self):
        self.items = []
        
    def add(self, product):
        self.items.append(product)
        product.reduce_stock()
        
    def remove(self, product):
        if product in self.items:
            self.items.remove(product)
            
    def checkout(self):
        total = 0
        print("Receipt")
        for p in self.items:
            price = p.get_discount_price()
            print(f"{p.name} : Rs {price:.2f}")
            total += price
        print("Total = Rs", total)
        
p1 = Electronics("Laptop", 50000, 5)
p2 = Clothing("Dress", 800, 2)
p3 = Grocery("Rice", 250, 1)

cart = ShoppingCart()
cart.add(p1)
cart.add(p2)
cart.add(p3)
cart.remove(p2)
cart.checkout()