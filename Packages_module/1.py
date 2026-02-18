from abc import ABC, abstractmethod

# class vehicle(ABC):
    
#     @abstractmethod
#     def start(self):
#         print("The car started")


#     @abstractmethod
#     def stop(self):
#         print("The car stopped")

# class BMW(vehicle):
#     def start(self):
#         print("The BMW car started")

#     def stop(self):
#         print("The BMW car stopped")

# car = BMW()
# car.start()
# car.stop()



# make a class paymentsystem

# class PaymentSystem(ABC):

#     @abstractmethod
#     def pay(self):
#         print("Payment made successfully")

# class CreditCard(PaymentSystem):
#     def pay(self):
#         print("Payment made successfully using Credit Card")

# class DebitCard(PaymentSystem):
#     def pay(self):
#         print("Payment made successfully using Debit Card")

# class Paytm(PaymentSystem):
#     def pay(self):
#         print("Payment made successfully using Paytm")

# payment = PaymentSystem()
# payment.pay()

# debit  = DebitCard()
# debit.pay()       

# credit = CreditCard()
# credit.pay()

# pay = Paytm()
# pay.pay()

# create a abstract class method -> book ticket
                                #  -> cancel ticket
                                #  -> flight 
                                #  -> train
                                #  -> bus



# class Ticket(ABC):

#     @abstractmethod
#     def book(self):
#         print("Ticket booked successfully")

#     @abstractmethod
#     def cancel(self):
#         print("Ticket cancelled successfully")


# class Flight(Ticket):
      
#     def book(self):
#            print("Flight ticket is booked")

#     def cancel(self):
#         print("Flight ticket is cancel")


# class Train(Ticket):
      
#     def book(self):
#            print("Train ticket is booked")

#     def cancel(self):
#         print("Train ticket is cancel")

# class Bus(Ticket):
      
#     def book(self):
#            print("Bus ticket is booked")

#     def cancel(self):
#         print("Bus ticket is cancel")


# f = Flight()
# f.book()
# f.cancel()

# t=Train()
# t.book()
# t.cancel()

# b=Bus() .
# b.book()
# b.cancel()


#  =================================
# Modules :-> Modules are the .py files which contains 
# functions, classes, variables, etc. which can be imported and used in other .py files.


# package -> package is a collection of modules.
# It is a way to organize the modules in a directory structure. 
# A package can contain __ini__.py file and sub-packages and modules.

# two types of packages :-> 1. Regular package
#                           2. Namespace package

# Regular package :-> A regular package is a package which contains __init__.py file.

# Namespace package :-> A namespace package is a package which does not contain __init__.py file.
# It is used to create a package which can be split across multiple directories. 
# It is used to create a package which can be distributed














