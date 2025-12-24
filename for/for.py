# 1. Stop when number becomes 6

for i in range(1, 11):
    if i == 6:
        break
    print(i)

# 2. Skip printing 5

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 3. Stop when number divisible by 7

for i in range(1, 21):
    if i % 7 == 0:
        break
    print(i)

# 4. Skip all even numbers

for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)

# 5. Stop when number becomes 25

for i in range(1, 51):
    if i == 25:
        break
    print(i)

# 6. Skip numbers divisible by 3

for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)

# 7. Stop when sum exceeds 50

total = 0
for i in range(1, 101):
    total += i
    if total > 50:
        break
    print(i)

# 8. Skip numbers divisible by 4 or 6

for i in range(1, 21):
    if i % 4 == 0 or i % 6 == 0:
        continue
    print(i)

# 9. Stop when number is multiple of 13

for i in range(1, 101):
    if i % 13 == 0:
        break
    print(i)

# 10. Skip numbers whose last digit is 5

for i in range(1, 51):
    if i % 10 == 5:
        continue
    print(i)

# 11. Stop when number is a perfect square

for i in range(1, 31):
    if int(i ** 0.5) ** 2 == i:
        break
    print(i)

# 12. Skip numbers whose square is divisible by 10

for i in range(1, 101):
    if (i * i) % 10 == 0:
        continue
    print(i)

# 13. Stop when user enters 0

while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    print(num)

# 14. Skip numbers divisible by both 3 and 5

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        continue
    print(i)

# 15. Stop when number contains digit 9

for i in range(1, 51):
    if '9' in str(i):
        break
    print(i)

# 16. Skip numbers whose sum of digits is even

for i in range(1, 21):
    s = sum(map(int, str(i)))
    if s % 2 == 0:
        continue
    print(i)

# 17. Stop when divisible by both 8 and 12

for i in range(1, 101):
    if i % 8 == 0 and i % 12 == 0:
        break
    print(i)

# 18. Skip perfect squares

for i in range(1, 51):
    if int(i ** 0.5) ** 2 == i:
        continue
    print(i)

# 19. Stop when number is a palindrome

for i in range(1, 101):
    if str(i) == str(i)[::-1] and i > 9:
        break
    print(i)

# 20. Skip numbers whose factorial > 100

import math

for i in range(1, 31):
    if math.factorial(i) > 100:
        continue
    print(i)



# 🔹 Basic for Loop and range() Usage

# 1. Print numbers from 1 to 10

for i in range(1, 11):
    print(i)

# 2. Print numbers from 0 to 5

for i in range(6):
    print(i)

# 3. Print numbers from 5 to 15

for i in range(5, 16):
    print(i)

# 4. Print numbers from 10 to 1

for i in range(10, 0, -1):
    print(i)

# 5. Print all even numbers between 1 and 20

for i in range(2, 21, 2):
    print(i)

# 6. Print all odd numbers between 1 and 20

for i in range(1, 21, 2):
    print(i)

# 7. Print numbers from 1 to 50, skipping multiples of 5

for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i)

# 8. Print numbers from 1 to 100 with a step of 10

for i in range(1, 101, 10):
    print(i)

# 9. Print square of numbers from 1 to 10

for i in range(1, 11):
    print(i * i)

# 10. Print cube of numbers from 1 to 5

for i in range(1, 6):
    print(i * i * i)

# 🔹 Aggregation and Counting

# 11. Sum of numbers from 1 to 10

total = 0
for i in range(1, 11):
    total += i
print(total)

# 12. Sum of even numbers from 1 to 20

total = 0
for i in range(2, 21, 2):
    total += i
print(total)

# 13. Multiplication table of 5

for i in range(1, 11):
    print(5 * i)

# 14. Multiplication tables from 1 to 3

for n in range(1, 4):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
    print()

# 15. Count numbers between 1 and 50

count = 0
for i in range(1, 51):
    count += 1
print(count)

# 16. Count even numbers between 1 and 100

count = 0
for i in range(2, 101, 2):
    count += 1
print(count)

# 🔹 Control Flow and Formatting

# 17. Stop printing when number becomes 20

for i in range(1, 31):
    if i == 20:
        break
    print(i)

# 18. Do not print 10

for i in range(1, 21):
    if i == 10:
        continue
    print(i)

# 19. Print numbers 1 to 5 (new line)

for i in range(1, 6):
    print(i)

# 20. Print numbers 1 to 5 in single line

for i in range(1, 6):
    print(i, end=" ")

# 21. Print numbers from 5 to 1

for i in range(5, 0, -1):
    print(i)

# 22. Print numbers with their squares

for i in range(1, 6):
    print(i, i * i)

# 🔹 Output Prediction and Execution Count

# ✅ Question 23

for i in range(3):
    print(i)



# 📤 Output
0
1
2

# ✅ Question 24

for i in range(1, 6, 2):
    print(i)


# 📤 Output
1
3
5


# 25. How many times will this loop execute?

for i in range(10):
    print(i)


# 🔹 Single For Loop – Level Up Answers (1–25)

# 1. Divisible by both 3 and 5

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# 2. Last digit is 7

for i in range(1, 51):
    if i % 10 == 7:
        print(i)

# 3. Exactly two digits

for i in range(1, 101):
    if 10 <= i <= 99:
        print(i)

# 4. Sum of squares (1 to 10)

total = 0
for i in range(1, 11):
    total += i * i
print(total)

# 5. Difference between sum of even and odd (1–20)

even_sum = 0
odd_sum = 0

for i in range(1, 21):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(even_sum - odd_sum)

# 6. Perfect squares (1–50)

for i in range(1, 51):
    if int(i ** 0.5) ** 2 == i:
        print(i)

# 7. Divisible by 6 but not by 12

for i in range(1, 101):
    if i % 6 == 0 and i % 12 != 0:
        print(i)

# 8. Count divisible by 7

count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1
print(count)

# 9. Palindrome numbers

for i in range(1, 101):
    if str(i) == str(i)[::-1]:
        print(i)

# 10. Product of numbers 1 to 5

product = 1
for i in range(1, 6):
    product *= i
print(product)

# 11. Sum of digits is 5

for i in range(1, 101):
    if sum(map(int, str(i))) == 5:
        print(i)

# 12. Largest number divisible by 9

largest = 0
for i in range(1, 101):
    if i % 9 == 0:
        largest = i
print(largest)

# 13. Divisible by 3 or 7 but not both

for i in range(1, 51):
    if (i % 3 == 0) ^ (i % 7 == 0):
        print(i)

# 14. Contain digit 3

for i in range(1, 101):
    if '3' in str(i):
        print(i)

# 15. Count even numbers

count = 0
for i in range(1, 101):
    if i % 2 == 0:
        count += 1
print(count)

# 16. Number of digits = 2

for i in range(1, 101):
    if len(str(i)) == 2:
        print(i)

# 17. Square less than 500

for i in range(1, 51):
    if i * i < 500:
        print(i)

# 18. Sum divisible by 4

total = 0
for i in range(1, 101):
    if i % 4 == 0:
        total += i
print(total)

# 19. Multiple of 8 but not 16

for i in range(1, 101):
    if i % 8 == 0 and i % 16 != 0:
        print(i)

# 20. Number × 2 ends with 4

for i in range(1, 101):
    if (i * 2) % 10 == 4:
        print(i)

# 21. Count numbers ending with 0

count = 0
for i in range(1, 101):
    if i % 10 == 0:
        count += 1
print(count)

# 22. Divisible by sum of digits

for i in range(1, 101):
    s = sum(map(int, str(i)))
    if s != 0 and i % s == 0:
        print(i)

# 23. Number + reverse is even

for i in range(1, 51):
    rev = int(str(i)[::-1])
    if (i + rev) % 2 == 0:
        print(i)

# 24. Triangular numbers

n = 0
for i in range(1, 101):
    n += i
    if n <= 100:
        print(n)

# 25. Smallest number divisible by both 6 and 8

for i in range(1, 101):
    if i % 6 == 0 and i % 8 == 0:
        print(i)
        break