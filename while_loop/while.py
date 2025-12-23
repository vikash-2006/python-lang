# 1 Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# 2 Print numbers from 0 to 5
i = 0
while i <= 5:
    print(i)
    i += 1

# 3 Print numbers from 5 to 15
i = 5
while i <= 15:
    print(i)
    i += 1

# 4 Print numbers from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

# 5 Print even numbers between 1 and 20
i = 2
while i <= 20:
    print(i)
    i += 2

# 6 Print odd numbers between 1 and 20
i = 1
while i <= 20:
    print(i)
    i += 2

# 7 Print numbers 1 to 50 with step 5
i = 1
while i <= 50:
    print(i)
    i += 5

# 8 Print squares 1 to 10
i = 1
while i <= 10:
    print(i*i)
    i += 1

# 9 Print cubes 1 to 5
i = 1
while i <= 5:
    print(i*i*i)
    i += 1

# 10 Sum from 1 to 10
i = 1
s = 0
while i <= 10:
    s += i
    i += 1
print(s)


# Output: 55

# 11 Sum of even numbers 1 to 20
i = 2
s = 0
while i <= 20:
    s += i
    i += 2
print(s)


# Output: 110

# 12 Multiplication table of 7
i = 1
while i <= 10:
    print(7, "x", i, "=", 7*i)
    i += 1

# 13 Multiplication table 1 to 3
i = 1
while i <= 3:
    j = 1
    while j <= 10:
        print(i, "x", j, "=", i*j)
        j += 1
    print()
    i += 1

# 14 Count numbers 1 to 50
i = 1
count = 0
while i <= 50:
    count += 1
    i += 1
print(count)


# Output: 50

# 15 Count even numbers 1 to 100
i = 1
count = 0
while i <= 100:
    if i % 2 == 0:
        count += 1
    i += 1
print(count)


# Output: 50

# 16 Stop at 20
i = 1
while i <= 30:
    if i == 20:
        break
    print(i)
    i += 1

# 17 Skip printing 10
i = 1
while i <= 20:
    if i == 10:
        i += 1
        continue
    print(i)
    i += 1

# 18 Print 1 to 5 new line
i = 1
while i <= 5:
    print(i)
    i += 1

# 19 Print 1 to 5 in single line
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1

# 20 Reverse 5 to 1
i = 5
while i >= 1:
    print(i)
    i -= 1

# 21 Print number and square from 1 to 10
i = 1
while i <= 10:
    print(i, i*i)
    i += 1

# 22 What will be the output?

# Code: 

i = 1
while i < 3:
    print(i)
    i += 1


# Output:

1
2

# 23 Output of
i = 1
while i <= 5:
    print(i)
    i += 2


# Output:

1
3
5

# 24 How many times loop runs?
i = 10
while i > 0:
    print(i)
    i -= 3


# Values printed:
10
7
4
1

# Loop runs 4 times.

# 25 Will this loop terminate?
i = 1
while i < 5:
    print(i)



# 1. Numbers from 1 to 100 divisible by 3

i = 1
while i <= 100:
    if i % 3 == 0:
        print(i)
    i += 1

# 2. Numbers from 1 to 50 divisible by 5 but not by 10

i = 1
while i <= 50:
    if i % 5 == 0 and i % 10 != 0:
        print(i)
    i += 1

# 3. Sum of digits of a number

n = int(input("Enter number: "))
s = 0

while n > 0:
    s += n % 10
    n //= 10

print("Sum of digits:", s)

# 4. Reverse a number

n = int(input("Enter number: "))
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print("Reverse:", rev)

# 5. Palindrome number

n = int(input("Enter number: "))
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# 6. Count digits

n = int(input("Enter number: "))
count = 0

while n > 0:
    count += 1
    n //= 10

print("Digits:", count)

# 7. Product of digits

n = int(input("Enter number: "))
prod = 1

while n > 0:
    prod *= n % 10
    n //= 10

print("Product:", prod)

# 8. Numbers from 1 to 100 whose last digit is 7

i = 1
while i <= 100:
    if i % 10 == 7:
        print(i)
    i += 1

# 9. Numbers from 1 to 100 containing digit 5

i = 1
while i <= 100:
    temp = i
    while temp > 0:
        if temp % 10 == 5:
            print(i)
            break
        temp //= 10
    i += 1

# 10. Sum of even digits

n = int(input("Enter number: "))
s = 0

while n > 0:
    d = n % 10
    if d % 2 == 0:
        s += d
    n //= 10

print("Sum of even digits:", s)

# 11. Factorial of a number

n = int(input("Enter number: "))
fact = 1

while n > 0:
    fact *= n
    n -= 1

print("Factorial:", fact)

# 12. Factors of a number

n = int(input("Enter number: "))
i = 1

while i <= n:
    if n % i == 0:
        print(i)
    i += 1

# 13. Perfect number

n = int(input("Enter number: "))
i = 1
s = 0

while i < n:
    if n % i == 0:
        s += i
    i += 1

if s == n:
    print("Perfect Number")
else:
    print("Not Perfect")

# 14. Perfect squares between 1 and 100

i = 1
while i * i <= 100:
    print(i * i)
    i += 1

# 15. Count numbers divisible by both 4 and 6 (1–100)

i = 1
count = 0

while i <= 100:
    if i % 4 == 0 and i % 6 == 0:
        count += 1
    i += 1

print("Count:", count)

# 16. Largest digit

n = int(input("Enter number: "))
largest = 0

while n > 0:
    d = n % 10
    if d > largest:
        largest = d
    n //= 10

print("Largest digit:", largest)

# 17. Smallest digit

n = int(input("Enter number: "))
smallest = 9

while n > 0:
    d = n % 10
    if d < smallest:
        smallest = d
    n //= 10

print("Smallest digit:", smallest)

# 18. Armstrong number

n = int(input("Enter number: "))
temp = n
count = 0
s = 0

while temp > 0:
    count += 1
    temp //= 10

temp = n
while temp > 0:
    d = temp % 10
    s += d ** count
    temp //= 10

if s == n:
    print("Armstrong Number")
else:
    print("Not Armstrong")

# 19. Numbers whose sum of digits is 10

i = 1
while i <= 100:
    temp = i
    s = 0
    while temp > 0:
        s += temp % 10
        temp //= 10
    if s == 10:
        print(i)
    i += 1

# 20. Sum of first N natural numbers

n = int(input("Enter N: "))
s = 0
i = 1

while i <= n:
    s += i
    i += 1

print("Sum:", s)

# 21. Numbers from 1 to N divisible by 2 and 5

n = int(input("Enter N: "))
i = 1

while i <= n:
    if i % 2 == 0 and i % 5 == 0:
        print(i)
    i += 1

# 22. Count odd digits

n = int(input("Enter number: "))
count = 0

while n > 0:
    if (n % 10) % 2 != 0:
        count += 1
    n //= 10

print("Odd digits:", count)

# 23. Divisible by exactly one of 3 or 7

i = 1
while i <= 100:
    if (i % 3 == 0 and i % 7 != 0) or (i % 7 == 0 and i % 3 != 0):
        print(i)
    i += 1

# 24. Reverse of numbers from 1 to 20

i = 1
while i <= 20:
    n = i
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    print(i, "->", rev)
    i += 1

# 25. Infinite or terminating?

i = 2
while i != 1:
    print(i)
    i += 2