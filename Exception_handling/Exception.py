# ============================================================
# EXCEPTION HANDLING IN PYTHON
# ============================================================

# Exceptions are unexpected errors that occur during
# the execution of a program.
# If exceptions are not handled, the program may crash.
# Python provides try, except, else, and finally blocks
# to handle exceptions gracefully.

# ============================================================
# BASIC STRUCTURE OF EXCEPTION HANDLING
# ============================================================

# try:
#     Code that may raise an exception
# except ExceptionType:
#     Code to handle the exception
# else:
#     Code that runs if no exception occurs
# finally:
#     Code that always executes

# ============================================================
# EXAMPLE 1: ZeroDivisionError
# ============================================================

try:
    a = 10
    b = 0
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

# ============================================================
# EXAMPLE 2: TypeError
# ============================================================

a = 10
b = "2"

try:
    result = a + b
    print(result)
except TypeError:
    print("Error: Please provide valid input types")

# ============================================================
# EXAMPLE 3: NameError
# ============================================================

a = 10

try:
    result = a + c
    print(result)
except NameError as e:
    print("NameError occurred:", e)

# ============================================================
# EXAMPLE 4: try-except-finally
# ============================================================

a = 10
b = "2"

try:
    result = a + b
    print(result)
except TypeError:
    print("Error: Invalid data type")
finally:
    print("Execution completed")

# ------------------------------------------------------------
# try     -> Wraps risky code
# except  -> Handles the error
# finally -> Always executes
# ------------------------------------------------------------

# ============================================================
# EXAMPLE 5: Handling IndexError
# ============================================================

li = [1, 2, 3, 4]

try:
    index = int(input("Enter index number: "))
    print("Element at index:", li[index])

except IndexError:
    print("IndexError: Please enter index between 0 and", len(li)-1)

except ValueError:
    print("ValueError: Please enter an integer value")

else:
    print("Access successful")

finally:
    print("Program execution completed")

# ============================================================
# EXAMPLE 6: ZeroDivisionError with else and finally
# ============================================================

try:
    n = int(input("Enter any number: "))
    result = 10 / n
    print("Result:", result)

except ZeroDivisionError as e:
    print("Error:", e)

except ValueError:
    print("Please enter a valid integer")

else:
    print("Calculation successful")

finally:
    print("This block always runs")

# ============================================================
# EXAMPLE 7: Handling KeyError in Dictionary
# ============================================================

data = {
    "name": "Vikash",
    "course": "BCA",
    "year": 2
}

try:
    key = input("Enter key to access: ")
    value = data[key]
    print("Value:", value)

except KeyError as e:
    print("KeyError: Key not found ->", e)

else:
    print("Key accessed successfully")

finally:
    print("Program execution completed")

# ============================================================
# EXAMPLE 8: Handling Wrong Input (ValueError)
# ============================================================

try:
    n = int(input("Enter a number: "))
    square = n * n
    print("Square:", square)

except ValueError:
    print("Error: Please enter a valid integer")

else:
    print("Square calculated successfully")

finally:
    print("Program execution completed")

# ============================================================
# COMMON EXCEPTION TYPES
# ============================================================

# ZeroDivisionError -> Divide by zero
# TypeError         -> Wrong data type
# ValueError        -> Invalid value
# IndexError        -> Invalid index
# KeyError          -> Key not found in dictionary
# NameError         -> Variable not defined

# ============================================================
# IMPORTANT EXAM POINTS
# ============================================================

# 1. try block must be followed by at least one except block
# 2. Multiple except blocks can be used
# 3. else block runs only if no exception occurs
# 4. finally block always executes
# 5. Exception handling prevents program termination
