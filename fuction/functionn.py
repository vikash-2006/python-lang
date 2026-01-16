# Function is a block of reusable code..whenever there is a
# task we call that function..
# On the time of function definition we give the parameters which are
# being used into the function..

# def keyword is used to define the function
# (parameters) -> def function_name(parameters):
#                 particular task

def coffee_machine(sugar, milk, beans):
    # Prepare beans
    print('Preparing Beans...')
    # Taking milk
    print('Mixing coffe with the milk')
    # coffee is ready
    print('Your coffee is ready...')
# function call -> at the time of function call we give the arguments
# name of the function(arguments)
coffee_machine('sugar', 'milk', 'beans')


# =============================================================================

def add(a, b):
    # Return keyword is used to return the value
    return a + b
    # when we are calling the function this returns a value..stored into the
    # variable sum
    # which we can use anywhere in our program

sum = add(3,4)

print('The sum is ', sum)
# (the sum is a+b)

# =============================================================================
# Simple Calculator using functions


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b


print("Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice (1-4): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", subtract(num1, num2))
elif choice == 3:
    print("Result:", multiply(num1, num2))
elif choice == 4:
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")

# =============================================================================

