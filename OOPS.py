#4 pillars of OOPS
# 1. Polymorphism
# 2. Encapsulation
# 3. Inheritance
# 4. Abstraction

"""Encapsulation"""
# class A:
#     def __init__(self,name,age,gender):     #__init__ is a constructor which is used to initialize the variables
#         self.__name = name                    # self is used to refer to the current object 
#         self._age = age
#         self.gender = gender
#     def display(self):
#         print(self.__name)
#         print(self._age)
#         print(self.gender)
#     def setAge(self,age):
#         self._age = age
#     def getAge(self):
#         return self._age 
#     def setName(self,name):
#         self.__name = name
#     def getName(self):
#         return self.__name
# a1 = A("Vijay", 21, "Male")
# a2 = A("Sushanth", 20, "Unknown")
# # print(a1.display())
# # a1.setAge(22)
# # print(a1.display())
# print(a2.display())
# a2.setName("penta paul")
# print(a2.display())


"""Abstraction - Hiding the implementation details and showing only the essential features"""
# from abc import ABC, abstractmethod     #abc is a module which is used to create abstract classes 
# class BankAccount(ABC):
#     def __init__(self, balance):
#         self.__balance = balance
#     def deposit(self, amount):
#         self.__balance += amount
#     def withdraw(self, amount):
#         self.__balance -= amount
#     def getBalance(self):
#         return self.__balance
#     @abstractmethod                          #@abstractmethod is a decorator which is used to create abstract methods 
#     def interestcalc(self):
#         pass
# class SavingAccount(BankAccount):
#     def interestcalc(self):
#         return (self.__balance * 0.05)

# u1 = SavingAccount(15000)
# print(u1.getBalance())
# u1.deposit(5000)
# print(u1.getBalance())
# u1.withdraw(2000)
# print(u1.getBalance())
# print(u1.interestcalc())

"""Polymorphism - one name many forms"""
class Animal:
    print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Woof")
class Cat(Animal):
    def sound(self):
        print("Meow")
a1 =  Animal()
a2 = Dog()
a3 = Cat()
a2.sound()
a3.sound()
