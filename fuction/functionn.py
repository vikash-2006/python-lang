# Function is a block of reusable code..whenever there is a
# task we call that function..
# On the time of function definition we give the parameters which are
# being used into the function..

# def keyword is used to define the function
# (parameters) -> def function_name(parameters):
#                 particular task

# def coffee_machine(sugar, milk, beans):
#     # Prepare beans
#     print('Preparing Beans...')
#     # Taking milk
#     print('Mixing coffe with the milk')
#     # coffee is ready
#     print('Your coffee is ready...')
# # function call -> at the time of function call we give the arguments
# # name of the function(arguments)
# coffee_machine('sugar', 'milk', 'beans')


# =============================================================================

# def add(a, b):
#     # Return keyword is used to return the value
#     return a + b
#     # when we are calling the function this returns a value..stored into the
#     # variable sum
#     # which we can use anywhere in our program

# sum = add(3,4)

# print('The sum is ', sum)
# # (the sum is a+b)

# # =============================================================================
# # Simple Calculator using functions


# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error: Division by zero"
#     else:
#         return a / b


# print("Calculator")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")

# choice = int(input("Enter your choice (1-4): "))

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if choice == 1:
#     print("Result:", add(num1, num2))
# elif choice == 2:
#     print("Result:", subtract(num1, num2))
# elif choice == 3:
#     print("Result:", multiply(num1, num2))
# elif choice == 4:
#     print("Result:", divide(num1, num2))
# else:
#     print("Invalid choice")

# =============================================================================

#  Default Keyword argument -->>  into this argument we pass the default value with parameter
# def greeting(name='User'):
#     return f"Hello there ..... YOU ARE {name}  How, may help you"
# name = input("Enter you name :- ")
# message = greeting()
# print(f"UI",  {message})

# print(f"DashBoard",  {message})


# =============================================================================

#  Positional argument, -->> argument which are passed at the time function callin
# in that position in which  the perameter are defined


# def greeting(name='User'):
#     return f"Hello there ..... YOU ARE {name}  How, may help you"
# name = input("Enter you name :- ")
# message = greeting(name)
# print(f"UI",  {message})

# print(f"DashBoard",  {message})


# =============================================================================

#  keyword argument -->> at the time  of functionn calling we pass the 
# values with the parameter name  -> location  =  'value'


# def show_details(name,location):

#     return f'Hello I am {name}.I belongs from {location}.'

# name = input("Enter your name :- ")
# location =  input("Enter your city :- ")
# msg = show_details(name = name, location = location)
# print(msg)

# =============================================================================


# write a function name age city print all info 

# def info(name = 'User', age='young', city = 'Jaipur'):
#     return f'My self {name}. i am {age} year old. And i am from {city}'
# name = input("Enter name :- ")
# age = int(input("Enter age :- "))
# city = input("Enter city name :- ")
# msg = info(name, age, city)
# print(msg)


# =============================================================================

# write a function area (len,width) defaul = 5

# def area(length, width = 5):

#     return f'The area is {length*width}'

# length = int(input("Enter length :- "))
# msg = area(length)
# print(msg)

# =============================================================================


#  write a function to display the details of the employees 
#  name,  dept, salary
#  call it with positional arrgument as well as keyword argument


# def info(name, dept, salary):
#     return f'Name :- {name}. Salary :-  {Salary} . Department :- {dept}'

# name = input("Enter name :- ")
# salary = int(input("Enter salary :- "))
# dept = input("Enter city name :- ")
# msg = info(name = name, salary = salary, dept=dept)
# print(msg)


# =============================================================================

# Global variable   -->> Which is accessable inside or  outside
# You can use this variable anywhere into the program
# If you want to the value of the global var then use global keyword to access the variable


var = 1
def count():
    # local variable is accessible only inside the function  we cant use use outside the function
    var2 = 2
    global var 
    var = 20
count()
print(var)


# =============================================================================

# Write a program to change the counter value of global variable
# First -> Count = 1, Second -> Count = 2
# count -> globle variable 

# Global variable
count = 1

def increase_count():
    global count
    count = count + 1
    print("Second -> Count =", count)

# First value
print("First -> Count =", count)

# Function call to change global variable
increase_count()
