# ===============================
# BASIC VARIABLES (Procedural Style)
# ===============================

name = "Vikash"
course = "BCA"
roll_num = 101
location = "Jaipur"

print("Name:", name)
print("Course:", course)
print("Roll Number:", roll_num)
print("Location:", location)


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

class House:
    
    # Class attributes (common for all objects)
    color = "Red"
    room = 5

    # Constructor (automatically called when object is created)
    def __init__(self, user_color):
        self.h_color = user_color     # Instance attribute
        print("House is created")
        print("This is a house")


# Creating objects of House class
house1 = House("Yellow")
house2 = House("Blue")

print(house1.h_color)
print(house1.room)
print(house2.color)


# ===============================
# CLASS EXAMPLE: EMPLOYEE
# ===============================

class Employee:
    
    # Class attribute (same for all employees)
    company = "ABC Technologies"
    
    # Constructor to initialize employee details
    def __init__(self, name, location, department, salary):
        self.name = name              # Employee name
        self.location = location      # Employee location
        self.department = department  # Employee department
        self.salary = salary          # Employee salary
    
    # Method to display employee details
    def display_details(self):
        print("Company     :", Employee.company)
        print("Name        :", self.name)
        print("Location    :", self.location)
        print("Department  :", self.department)
        print("Salary      :", self.salary)


# Creating object of Employee class
emp1 = Employee("Rahul", "Delhi", "IT", 50000)

# Calling method
emp1.display_details()


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
class Animal:
    def sound(self):
        print("Animal makes a sound")


# Child class
class Dog(Animal):
    pass


# Creating object of Dog class
dog = Dog()

# Calling inherited method
dog.sound()

