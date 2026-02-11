# ===============================
# BASIC VARIABLES (Procedural Style)
# ===============================

# name = "Vikash"
# course = "BCA"
# roll_num = 101
# location = "Jaipur"

# print("Name:", name)
# print("Course:", course)
# print("Roll Number:", roll_num)
# print("Location:", location)


# ===============================
# WHY WE USE OOPs?
# ===============================

# Problem with Procedural Programming:
# -> We cannot manage each variable or entity separately.
# -> Code becomes hard to maintain for large programs.

# Solution:
# -> OOPs (Object-Oriented Programming) helps us manage and organize
#    code by encapsulating data and behavior into objects.


# ===============================
# BASIC OOPs CONCEPTS
# ===============================

# class -> A blueprint for creating objects.
#          It defines attributes (variables) and methods (functions).

# self  -> Represents the current object (instance of the class).
#          It allows access to attributes and methods of the class.


# ===============================
# FOUR PRINCIPLES OF OOPs
# ===============================

# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction


# ===============================
# CLASS EXAMPLE: HOUSE
# ===============================

# class House:
    
#     # Class attributes (common for all objects)
#     color = "Red"
#     room = 5

#     # Constructor (automatically called when object is created)
#     def __init__(self, user_color):
#         self.h_color = user_color     # Instance attribute
#         print("House is created")
#         print("This is a house")


# # Creating objects of House class
# house1 = House("Yellow")
# house2 = House("Blue")

# print(house1.h_color)
# print(house1.room)
# print(house2.color)


# ===============================
# CLASS EXAMPLE: EMPLOYEE
# ===============================

# class Employee:
    
#     # Class attribute (same for all employees)
#     company = "ABC Technologies"
    
#     # Constructor to initialize employee details
#     def __init__(self, name, location, department, salary):
#         self.name = name              # Employee name
#         self.location = location      # Employee location
#         self.department = department  # Employee department
#         self.salary = salary          # Employee salary
    
#     # Method to display employee details
#     def display_details(self):
#         print("Company     :", Employee.company)
#         print("Name        :", self.name)
#         print("Location    :", self.location)
#         print("Department  :", self.department)
#         print("Salary      :", self.salary)


# # Creating object of Employee class
# emp1 = Employee("Rahul", "Delhi", "IT", 50000)

# # Calling method
# emp1.display_details()


# ===============================
# INHERITANCE
# ===============================

# Inheritance:
# -> A mechanism where a child class inherits properties and methods
#    from a parent class.

# Parent class -> The class being inherited from
# Child class  -> The class that inherits


# Types of Inheritance:
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance


# ===============================
# INHERITANCE EXAMPLE
# ===============================

# Parent class
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")


# # Child class
# class Dog(Animal):
#     pass


# # Creating object of Dog class
# dog = Dog()

# # Calling inherited method
# dog.sound()




# Super Keyword: -->

# similar to self, but it is used to refer to the parent class.


# Single Inheritance -->> only one parent class is inherited by the child class.




# class Parent:
#     def __init__(self, name, location):
#         self.father_name = name
#         self.father_loc = location

#     def prp(self):
#         print("This is the father property!")


# class Child(Parent):
#     def __init__(self, child_name, father_name, location):
#         super().__init__(father_name, location)
#         self.child_name = child_name

#     def display_child(self):
#         print("Child Name :-", self.child_name)
#         print("Father Name :", self.father_name)
#         print("Father Location :", self.father_loc)


# # Object creation
# obj = Child("Naman", "Aman", "Delhi")

# # Access parent property
# print(obj.father_name)
# print(obj.father_loc)

# # Call child method
# obj.display_child()





# ======================================================
# MULTIPLE INHERITANCE EXAMPLE
# ======================================================

# Parent Class 1
class Mother:
    def __init__(self, name):
        # Instance attribute for mother's name
        self.mother_name = name

    def mother_prop(self):
        # Method of Mother class
        print("This is the mother property!")

    def display(self):
        # Method that may conflict in multiple inheritance
        print("This is the mother display method!")


# Parent Class 2
class Father:
    def __init__(self, name):
        # Instance attribute for father's name
        self.father_name = name

    def father_prop(self):
        # Method of Father class
        print("This is the father property!")

    def display(self):
        # Method that may conflict in multiple inheritance
        print("This is the father display method!")


# Child Class inheriting from both Mother and Father
class Child(Mother, Father):

    def __init__(self, m_name, f_name):
        # Calling Mother class constructor
        Mother.__init__(self, m_name)

        # Calling Father class constructor
        Father.__init__(self, f_name)

    def display(self):
        # Overriding display() method
        print("Mother Name :", self.mother_name)
        print("Father Name :", self.father_name)


# Creating object of Child class
obj = Child("Sita", "Ram")

# Calling parent methods
obj.mother_prop()
obj.father_prop()

# Calling overridden method
obj.display()



# ======================================================
# METHOD RESOLUTION ORDER (MRO)
# ======================================================

# MRO defines the order in which Python searches classes
# when a method is called in multiple inheritance.

class Mother:
    def show(self):
        print("This is Mother class")


class Father:
    def show(self):
        print("This is Father class")


# Child inherits Father first, then Mother
class Child(Father, Mother):
    pass


# Checking Method Resolution Order
print("MRO Order:", Child.mro())

# If we call show(), Python will search in this order:
# Child → Father → Mother → object



# ======================================================
# MULTILEVEL INHERITANCE
# ======================================================

# GrandFather → Father → Child


# Base Class
class GrandFather:
    def grand_father(self):
        print("This is the grandfather's property!")


# Father class inherits from GrandFather
class Father(GrandFather):
    def father_prop(self):
        print("This is the father's property!")


# Child class inherits from Father
class Child(Father):
    def child_prop(self):
        print("This is the child's property!")


# Creating object of Child class
obj = Child()

# Accessing methods from all levels
obj.grand_father()   # From GrandFather
obj.father_prop()    # From Father
obj.child_prop()     # From Child
