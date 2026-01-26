# ============================================================
# LAMBDA FUNCTION IN PYTHON
# ============================================================

# A lambda function is a small, anonymous function.
# It is used when a function is required for a short period.
# Lambda functions are written in a single line.
# They do NOT have a function name.
# They always return a value.
# Lambda functions are defined using the 'lambda' keyword.

# ------------------------------------------------------------
# SYNTAX:
# lambda parameters : expression
# ------------------------------------------------------------

# Example:
# lambda a, b : a + b


# ============================================================
# BASIC EXAMPLES OF LAMBDA FUNCTION
# ============================================================

# 1. Addition of two numbers
sum1 = lambda a, b: a + b
print(sum1(5, 6))      # Output: 11


# 2. Product of two numbers
product = lambda a, b: a * b
print(product(5, 6))  # Output: 30


# 3. Square of a number
square = lambda n: n * n
print(square(4))      # Output: 16


# 4. Check even or odd
even_odd = lambda n: 'Even' if n % 2 == 0 else 'Odd'
print(even_odd(5))    # Output: Odd


# 5. Check positive or negative number
pos_neg = lambda n: 'Positive' if n >= 0 else 'Negative'
print(pos_neg(-3))    # Output: Negative


# 6. Voting eligibility
vote = lambda age: 'Eligible to vote' if age >= 18 else 'Not eligible to vote'
print(vote(20))       # Output: Eligible to vote


# 7. Pass or Fail
pass_fail = lambda marks: 'Pass' if marks >= 40 else 'Fail'
print(pass_fail(35))  # Output: Fail


# ============================================================
# LAMBDA FUNCTION WITH MAP()
# ============================================================

# map() applies a function to each element of an iterable

# Syntax:
# map(function, iterable)

li = [10, 20, 30, 40, 50]

# Square each number
squares = list(map(lambda n: n * n, li))
print(squares)        # Output: [100, 400, 900, 1600, 2500]


# Convert Celsius to Fahrenheit
li_temp = [0, 20, 30, 40]
fahrenheit = list(map(lambda t: (t * 9/5) + 32, li_temp))
print(fahrenheit)     # Output: [32.0, 68.0, 86.0, 104.0]


# ============================================================
# LAMBDA FUNCTION WITH FILTER()
# ============================================================

# filter() selects elements based on a condition

# Syntax:
# filter(function, iterable)

li = [1,2,3,4,5,6,7,8,9,10]

# Get even numbers
even_numbers = list(filter(lambda n: n % 2 == 0, li))
print(even_numbers)   # Output: [2, 4, 6, 8, 10]


# Get odd numbers
odd_numbers = list(filter(lambda n: n % 2 != 0, li))
print(odd_numbers)    # Output: [1, 3, 5, 7, 9]


# ============================================================
# LAMBDA FUNCTION WITH SORTED()
# ============================================================

# Sort list of tuples based on second value
data = [(1, 3), (4, 1), (2, 2)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)    # Output: [(4, 1), (2, 2), (1, 3)]


# ============================================================
# IMPORTANT POINTS ABOUT LAMBDA FUNCTION
# ============================================================

# 1. Lambda functions can have any number of parameters.
# 2. They contain only ONE expression.
# 3. No return keyword is used.
# 4. Best suited for small, temporary operations.
# 5. Commonly used with map(), filter(), and sorted().