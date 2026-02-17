# Decorators -->> are the higher order functions that take another
# function as an argument which change the function  by the 
# exesting without changing the source code of the function being decorated.

# Decorator function

# def add_fun(fun):
#     def add_func():
#         print("This is the message")
#         fun()
#     return add_func



# @add_fun
# def hello():
#     print("This is the message")
#     print("Hello from the hello function")

# hello()

# =================================================\


# def my_decorator(gift):
#     def wrapper():
#         print("Adding some extra features to the gift function")
#         gift()
#         print("This is the end of the gift function")
#     return wrapper


# @my_decorator
# def gift():
#     print("This IS a book")


# gift()


# =================================================\

# write a decorator function that prints 'function started' before the execution of the function.

# def dec(fun):
#     def wrapper():
#         print("Function started")
#         fun()
#     return wrapper


# @dec
# def hh():
#     print("This is the hh function")

# 
#hh()

# =================================================\

# create a decorator function with checker function that checks 
# if the number is even before calling the function.



# def even_checker(fun):
#     def func(n):
#         if n % 2 == 0:
#             print("The number is even")
#             fun(n)
#         else:
#             print("The number is not even")
#             fun(n)
#     return func


# @even_checker
# def display(n):
#     print(f"The number is {n}")
# display(4)


# =================================================\


# question 1: 

# is_permitted = False
# def permission_required(func):
#     def wrapper():
#         if is_permitted:
#             print("Permission granted")
#             func()
#         else:
#             print("Permission denied")
#     return wrapper


# @permission_required
# def Data():
#     print("This is the secret data function")

# Data()



# ITERATOR -->> is an object that can be iterated upon, 
# meaning that you can traverse through all the values.

li = [1, 2, 3, 4, 5]
# Here we have made the normal list but we can make 
# it an iterator by using the iter() function.


iterable=iter(li)
print(next(iterable))
# next() function is used to get the next item from the iterator.
print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))
