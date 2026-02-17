# Polymorphism in Python

# Polymorphism in Python is an object-oriented programming concept that allows a single function,
# method, or operator to behave differently depending on the type or class of the object 
# it is operating on . 


# types of polymorphism in Python include: 

# method overloading
#  --> same name of the method (function ) but different parameters.

#  -->>  Python does not support method overloading in the traditional 
# sense (like in C++ or Java) primarily due to its dynamic typing and 
# how it manages namespaces. In Python, you can define a method with the same name multiple times,



# method overriding
# --> 

# class Animal:
#     # make sound method
#     def speak(self):
#         print( "Animal speaks")

# # Inheritance the animal class into the dog
# class Dog(Animal):

#     # here we define the same method name as the parent class but with different implementation
#     def speak(self):
#         print("Dog barks! ")

# class Cat(Animal):
#     def speak(self):
#         print("Cat meows! ")

# Dog = Dog()
# cat = Cat()
# Dog.speak()  # Output: Animal speaks
# cat.speak()  # Output: Dog barks!


# class shape:
#     def area(self):
#         print("Area of the shape")

# class circle(shape):
#     def area(self, radius):
#         area = 3.14 * radius * radius
#         print(f"Area of the circle with radius {radius} is: {area}")

# class square(shape):
#     def area(self, side):
#         area = side * side
#         print(area)

# cricle = circle()   
# cricle.area(1)  # Output: Area of the shape
# sq = square()  # Output: Area of the shape
# sq.area(4)  # Output: Area of the shape



# create a parent class with method introduce
# and override with it student and teacher class


# class Person:
#     def introduce(self):
#         print("Hello, I am a person.")

# class Student(Person):
#     def introduce(self):
#         print("Hello, I am a student.")
    
# class Teacher(Person):
#     def introduce(self):
#         print("Hello, I am a teacher.")

# student = Student()
# teacher = Teacher()
# student.introduce()  # Output: Hello, I am a student.
# teacher.introduce()  # Output: Hello, I am a teacher.



# create a parent class device with method power_on
# overide it with laptop and smartphone class


# class Device:
#     def power_on(self):
#         print("The device is powering on.")
    
# class Laptop(Device):
#     def power_on(self):
#         print("The laptop is powering on.")

# class smart_phone(Device):
#     def  power_on(self):
#         print("The smartphone is powering on.")

# obj = Device()

# obj1 = Laptop()

# obj1.power_on()  # Output: The laptop is powering on.

# obj2 = smart_phone()

# obj2.power_on()  # Output: The smartphone is powering on.


# create a parent class bank with method calculate_interest.
# SavingsAccount 
# CurrentAccount
# FixedDepositAccount

class Bank:
    def __init__(self, amount, rate, time):
        self.amount = amount
        self.rate = rate
        self.time = time
        print("Calculating interest for the bank account.")

class SavingsAccount(Bank):
    def calculate_interest(self):
        interest = (self.amount * self.rate * self.time) / 100
        print(f"Interest for the savings account: {interest}")

class CurrentAccount(Bank):
    def calculate_interest(self):
        interest = (self.amount * self.rate * self.time) / 100
        print(f"Interest for the current account: {interest}")

class FixedDepositAccount(Bank):
    def calculate_interest(self):
        interest = (self.amount * self.rate * self.time) / 100
        print(f"Interest for the fixed deposit account: {interest}")


# Objects
savings = SavingsAccount(1000, 5, 2)
savings.calculate_interest()

cur = CurrentAccount(2000, 4, 3)
cur.calculate_interest()

fix = FixedDepositAccount(5000, 6, 5)
fix.calculate_interest()

 