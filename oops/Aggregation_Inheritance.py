### Class Relationships

# - Aggregation
# - Inheritance

# example
# class Customer:

#   def __init__(self,name,gender,address):
#     self.name = name
#     self.gender = gender
#     self.address = address

#   def print_address(self):
#     print(self.address._Address__city,self.address.pin,self.address.state)

#   def edit_profile(self,new_name,new_city,new_pin,new_state):
#     self.name = new_name
#     self.address.edit_address(new_city,new_pin,new_state)

# class Address:

#   def __init__(self,city,pin,state):
#       self.__city = city
#       self.pin = pin
#       self.state = state

#   def get_city(self):
#     return self.__city

#   def edit_address(self,new_city,new_pin,new_state):
#     self.__city = new_city
#     self.pin = new_pin
#     self.state = new_state

# add1 = Address('gurgaon',122011,'haryana')
# cust = Customer('nitish','male',add1)

# cust.print_address()

# cust.edit_profile('ankit','mumbai',111111,'maharastra')
# cust.print_address()
# method example
# what about private attribute

# ================================================

##### Aggregation class diagram

### Inheritance

# - What is inheritance
# - Example
# - What gets inherited?

# Inheritance and it's benefits


# parent class
# class user:

#     def __init__(self):
#         self.name = 'Vikash'
#         self.gender = 'Male'


#     def log_in(self):
#         print('logged in successfully')
        
#  # child class
# class student(user):

#     # def  __init__(self):
#     #     self.roll_no = 101
#     #     self.marks = 90


#     def enroll(self):
#         print('enrolled successfully')


# u = user()
# s = student()

# print(s.name)
# print(s.gender)
# s.log_in()
# s.enroll() 

# ================================================

##### What gets inherited?

# - Constructor
# - Non Private Attributes
# - Non Private Methods

# ================================================

# constructor example

# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     pass

# s=SmartPhone(20000, "Apple", 13)
# s.buy()

# ================================================


# constructor example 2

# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

# class SmartPhone(Phone):
#     def __init__(self, os, ram):
#         self.os = os
#         self.ram = ram
#         print ("Inside SmartPhone constructor")

# s=SmartPhone("Android", 2)
# s.brand()

# child can't access private members of the class


# ================================================

# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     #getter
#     def show(self):
#         print (self.__price)

# class SmartPhone(Phone):
#     def check(self):
#         print(self.__price)

# s=SmartPhone(20000, "Apple", 13)
# s.show()
# s.check()  -->> AttributeError: 'SmartPhone' object has no attribute '_SmartPhone__price'
# --> parent class ke private attribute ko child class access nahi kar sakta hai.

# ================================================
# ================================================

# class Parent:

#     def __init__(self,num):
#         self.__num=num

#     def get_num(self):
#         return self.__num

# class Child(Parent):

#     def show(self):
#         print("This is in child class")
        
# son=Child(100)
# print(son.get_num())
# son.show()


# ================================================



# class Parent:

#     def __init__(self,num):
#         self.__num=num

#     def get_num(self):
#         return self.__num

# class Child(Parent):

#     def __init__(self,val,num):
#         self.__val=val

#     def get_val(self):
#         return self.__val
        
# son=Child(100,10)
# # print("Parent: Num:",son.get_num()) -->> not call because parent constructor is not called in child class
# print("Child: Val:",son.get_val())


# ================================================


# class A:
#     def __init__(self):
#         self.var1=100

#     def display1(self,var1):
#         print("class A :", self.var1)
# class B(A):
  
#     def display2(self,var1):
#         print("class B :", self.var1)

# obj=B()
# obj.display1(200)

# ================================================

# Method Overriding
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print ("Buying a smartphone")

# s=SmartPhone(20000, "Apple", 13)

# s.buy()




# ================================================

### Super Keyword


# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print ("Buying a smartphone")
#         # syntax to call parent ka buy method
#         super().buy()

# s=SmartPhone(20000, "Apple", 13)

# s.buy()


# ================================================



# using super outside the class
# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print ("Buying a phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print ("Buying a smartphone")
#         # syntax to call parent ka buy method
#         super().buy()

# s=SmartPhone(20000, "Apple", 13)

# s.buy()
# ================================================



# super -> constuctor

# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

# class SmartPhone(Phone):
#     def __init__(self, price, brand, camera, os, ram):
#         print('Inside smartphone constructor')
#         super().__init__(price, brand, camera)
#         self.os = os
#         self.ram = ram
#         print ("Inside smartphone constructor")

# s=SmartPhone(20000, "Samsung", 12, "Android", 2)

# print(s.os)
# print(s.brand)




# ================================================


##### Inheritance in summary

# - A class can inherit from another class.

# - Inheritance improves code reuse

# - Constructor, attributes, methods get inherited to the child class

# - The parent has no access to the child class

# - Private properties of parent are not accessible directly in child class

# - Child class can override the attributes or methods. This is called method overriding

# - super() is an inbuilt function which is used to invoke the parent class methods and constructor




# ================================================


class Parent:

    def __init__(self,num):
      self.__num=num

    def get_num(self):
      return self.__num

class Child(Parent):
  
    def __init__(self,num,val):
      super().__init__(num)
      self.__val=val

    def get_val(self):
      return self.__val
      
son=Child(100,200)
print(son.get_num())
print(son.get_val())



# ================================================


# class Parent:
#     def __init__(self):
#         self.num=100

# class Child(Parent):

#     def __init__(self):
#         super().__init__()
#         self.var=200
        
#     def show(self):
#         print(self.num)
#         print(self.var)

# son=Child()
# son.show()



# ================================================


# class Parent:
#     def __init__(self):
#         self.__num=100

#     def show(self):
#         print("Parent:",self.__num)

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__var=10

#     def show(self):
#         print("Child:",self.__var)

# obj=Child()
# obj.show()



# ================================================


### Types of Inheritance

# - Single Inheritance
# - Multilevel Inheritance
# - Hierarchical Inheritance
# - Multiple Inheritance(Diamond Problem)
# - Hybrid Inheritance



# ================================================


# single inheritance
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()




# ================================================


# multilevel
class Product:
    def review(self):
        print ("Product customer review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()



# ================================================

# Hierarchical
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()
FeaturePhone(10,"Lava","1px").buy()


# ================================================

