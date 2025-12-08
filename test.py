# FACTORIAL
# n = int(input("Enter the number :- "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# FABONACCI
# n=int(input("Enter the number :- "))
# print("FABONACCI SERIES :- ")
# a=0
# b=1

# for i in range(n+1):
#     a,b=a+b
#     print(b ,end=' ')

# DIGIT COUNT ......

# n = int(input("Enter the number :- "))
# count=0
# if n==0:
#     count=1
#     print("The digits are :- ",count)
# elif n<0:
#     print("Invalid Input")
# else:
#     while n!=0:
#         count+=1
#         n=n//10
#     print("The digits are :- ",count)
# 

#SUM OF DIGITS

# n = int(input("Enter the number :- "))
# sum=0
# while n!=0:
#     d=n%10
#     sum = sum + d
#     n=n//10
# print("The digits are :- ",sum)

#   LCM FINDING BETWEEN TWO NUMBERS :----

# a = int(input("Enter the number :- "))
# b = int(input("Enter the number :- "))
# lcm = 0
# if a > b:
#     lcm = a
# else:
#     lcm = b

# while True:
#     if lcm%a==0 and lcm%b==0:
#         print("The lcm is :- ",lcm)
#         break
#     lcm+=1


# def fact():
#     pro = 1
#     n = int(input("\nEnter the number :- "))
#     if n < 0:
#         print("\nInvalid Input.....")
#     else:
#         for i in range(1, n + 1):
#             pro *= i
#         print("\nThe FACTORIAL is :- ", pro)


# def prime():
#     n = int(input("\nEnter the number :- "))
#     if n < 0:
#         print("\nInvalid input........")
#     else:
#         count = 0
#         for i in range(2, n // 2 + 1):
#             if n % i == 0:
#                 count = 1
#                 break
#         if count == 0:
#             print("\n", n, "is PRIME number.....")
#         else:
#             print("\n", n, "is not PRIME number.....")


# def even():
#     n = int(input("\nEnter the number :- "))
#     if n < 1:
#         print("\nThis is not valid....")
#     else:
#         if n % 2 == 0:
#             print("\n", n, "is EVEN number.....")
#         else:
#             print("\n", n, "is ODD number......")


# print("\n*********** MENU DRIVEN **********")
# print("Press 1 for check EVEN/ODD ")
# print("Press 2 for check PRIME ")
# print("Press 3 for find FACTORIAL ")
# print("Press 4 for EXIT ")

# ch = int(input("\nEnter the choice :- "))

# if ch == 1:
#     even()
# elif ch == 2:
#     prime()
# elif ch == 3:
#     fact()
# elif ch == 4:
#     exit()
# else:
#     print("Invalid Input...")

# .........PATTERNS...........

# n = int(input("Enter the number :- "))

#======================================================
#======================================================
#======================================================

# STRING

# st = "hello world"
# print(st[0:5])

#======================================================
# var = input("Enter the string :- ")
# print(var[1:len(var)-1])

#======================================================
# l = "PythonProgramming"
# print(l[:6])
# print(l[6:])

#======================================================
# k = input("Enter the string :- ")
# print(k[0:len(k):2])
# for i in range(0, len(k), 2):
#     print(k[i], end='')
#======================================================
# o = "apple"
# print(o[::-1])

#======================================================
# st = "PythonProgramming"
# print(st[-11:-8])

#======================================================
# tt= "This is sentence"
# print(tt[-8:])

#======================================================
# yt = input("Enter the string :- ")
# print(yt[::2])

#======================================================
# i = "LearningPython"
# print(i[-6:])

#======================================================
# n =  input("Enter the string :- ")
# l = len(n)//2
# print(n[:l])
# print(n[l:])

#======================================================
# n = "DataScience"
# print(n[4:])

#======================================================
# n = input("Enter the string :- ")
# i = int(input("Enter the index :- "))
# print(n[:i])

#======================================================
# st = "String"
# print(st.isalpha())

#======================================================
# st = "SlicingExamples"
# print(st[0:len(st):2])

#======================================================
# st = input("Enter a string :- ")
# print(st[:3])
# print(st[-3:])

#======================================================
# st = "abcdefghijklmnop"
# print(st[6:11])

#======================================================
# st = input("Enter the string :- ")
# print(st[-4:])

#======================================================
# st = "OpenAIChatGPT"
# print(st[0:7])
# print(st[4:10])
# print(st[::-1])

#======================================================
# st = input("Enter the string :- ")
# print(st[2:len(st)-2]) 

#======================================================
# st = "ABCDEFG"
# print(st[0:len(st):2])

#======================================================
# st = input("Enter the string :- ")
# new = st[::-1]

#======================================================
# if new == st:
#     print("Palindrome")
# else:
#     print("Not Palindrome")\

#======================================================
# st = "HelloPython"
# print(st[3:7])

#======================================================
# st = input("Etner a string :- ")
# for ch in st:
#     print(ch*2, end = "")

# ======================================================
# ======================================================
# st = "ashaa"
# count=0
# for i in st:
#     count+=1
# print("The length of string is :- ",count)

#======================================================
# st = input("Enter the string :- ")
# sum=0
# for ch in st:
#     if ch.isdigit():
#         sum+=int(ch)
# print("The sum of digits are :- ",sum)

#======================================================
# st = input("Enter the string :- ")
# for ch in st:
#     if ch.isupper():
#         print(ch.lower(), end='')
#     elif ch.islower():
#         print(ch.upper(), end='')
#     else:
#         print(ch, end='')

#======================================================
# st = input("Enter the string :- ")
# st1=''
# for i in range(0,len(st)):
#     if i%2==0:
#         st1 = st1 + st[i].upper()
#     else:
#         st1  = st1 + st[i]
# print(st1)

#======================================================
# for ch in st:
#     if ch==lent:
#         print("length  is fullfilled")
#     elif ch.isupper():
#         upper =  False
#     elif ch.islower():
#         lower = False
     
#======================================================
# sent = "This is sentence".split()
# sent1 = ""

# for ch in sent:
#     sent1 =sent1 + ch[::-1] + " "

# print(sent1)

#======================================================
# st = input("Enter a string :- ")
# count=0
# for ch in st:
#     if ch.isnumeric():
#         count+=1
# print("The number of digits is :- ",count)

#======================================================
# t = input("Enter a string :- ")
# print(t[:3])
# print(t[-3:])

#======================================================
# text = "Hello world this is python"
# new = text.replace(" ","_")
# print(new)

#======================================================
# st = input("Enter a upper case string :- ")
# new=st.lower()
# print(new)

#======================================================
# st = input("Enter a string :- ")
# count = 0
# for ch in st:
#     count+=1
# print(count)

#======================================================
# sent = "This is a sentence. This is true statement".split()
# print(sent)
# max_len = 0
# for ch in sent:
#     if max_len < len(ch):
#         max_len = len(ch)
# print("The length is :- ",max_len)

# for word in sent:
#     if max_len == len(word):
#         print("The word is :- ",word)

#======================================================

# st = input("Enter a string :- ")
# no_vowel = 0
# no_const = 0
# no_digit = 0
# no_special = 0
# vowel = "aeiouAEIOU"

# for ch in st:
#     if ch.isalpha():
#         if ch in vowel:
#             no_vowel += 1
#         else:
#             no_const += 1
#     elif ch.isdigit():
#         no_digit += 1
#     else:
#         no_special += 1

# print("Number of vowels is :- ",no_vowel)
# print("Number of consonants is :- ",no_const)
# print("Number of digits is :- ",no_digit)
# print("Number of special symbol is :- ",no_special)

#======================================================

# valid_length = False
# has_upper = False
# has_lower = False
# has_digit = False
# has_special = False
# password = input("Enter the password :- ")
# if len(password) >= 8:
#     valid_length = True

# for c  in password:
#     if c.isupper():
#         has_upper = True
#     elif c.islower():
#         has_lower = True
#     elif c.isdigit():
#         has_digit = True
#     elif not c.isalnum():
#         has_special = True
# if valid_length and has_upper and has_lower and has_digit and has_special:
#     print("Strong Password")
# else:
#     print("Weak Password")

# if valid_length < 8:
#     print("Password must be at least 8 characters long.")
# elif has_upper == False:
#     print("Password must contain at least one uppercase letter.")
# elif has_lower == False:
#     print("Password must contain at least one lowercase letter.")
# elif has_digit == False:
#     print("Password must contain at least one digit.")
# elif has_special == False:
#     print("Password must contain at least one special character.")

#======================================================

# 1. Even Index Characters (Reverse Order) 2 Marks)
# Take a string input an
# d create a new string using characters from even index positions only, then print the
# result in reverse order using loops.

# st = input("Enter a string :- ")
# print(st[::-2])

#======================================================

# 2. Vowel-based Word Count (2 Marks) Count how many words in a sentence star
# t AND end with a vowel (case-insensitive).

# st = input("Enter a string :- ")
# count = 0
# vowel = "AEIOUaeiou"
# for ch in st:
#     if ch in vowel:
#         count+=1
# print("The number of vowel is :- ",count)

#======================================================

# 3. Palindrome Words (2 Marks)
# Print all palindrome words found in a given sentence

# sent = input("Enter a sentence :- ")
# st = sent.split()
# for word in st:
#     rev =  word[::-1]
#     if rev.lower() == word.lower():
#         print("The palindrome word is :- ",word)

#======================================================

# 4. Title Case Without split() or title() 3 Marks)
# Convert an entire sentence into Title Case using loops only.

# sent = input("Enter a sentence :- ")
# sent = sent.title()
# print(sent)

#======================================================

# 5. Reverse String Without Slicing 2 Marks)
# Reverse a string using loops only

# st = "Banana"
# rev = ""
# for ch in st:
#     rev = ch + rev
# print(rev)

#======================================================

# 6. Reverse Each Word Keep Word Order Same) 3 Marks)
# Example: "Python is Awesome" → "nohtyP si emosewA"

# st = input("Enter a sentence :- ").split()
# for i in st:
#     rev =  ""
#     rev =  i[::-1] + rev
#     print(rev, end = " ")

#==============================================================

# 7. Longest & Smallest Word in Sentence 3 Marks)
# Input a sentence, then find and print the longest 
# and smallest word without using built-ins like max() or sort().

# st =input("Enter a sentence :-").split()
# maxx_len = 0

# MAXIMUM

# for i in st:
#     if maxx_len < len(i):
#         maxx_len = len(i)
# print("The maximum length is :- ",maxx_len)

# FOR GETTING WORD

# for word in st:
#     if maxx_len == len(word):
#         print("The word is :-",word)

#FOR MINIMUM

# minn_len = maxx_len
# for i in st:
#     if len(i) < minn_len:
#         minn_len = len(i)
# print("The minimum length is :- ",minn_len)

# FOR GETTING WORD

# for word in st:
#     if minn_len == len(word):
#         print("The word is :-",word)

#==============================================================

# 8. Count Consonants in a String 3 Marks)
# Take a string input and count how many consonants
# it contains using loops.

# st = input("Enter a string :- ")

# count = 0
# vowel = "aeiouAEIOU"

# for i in st:
#     if i in vowel:
#         pass
#     else:
#         count += 1
# print("The consonant number in sentence is :- ",count) 

#===========================================================================

# Section B Number-Based Problems 20 Marks)


# 9. Prime Digits Count 2 Marks)
# Take a numeric string and count how many digits are prime (2, 3, 5, 7)

# st = "prime23576"
# count = 0
# l = len(st)

# for i in st:
#     if i.isdigit():
#         num = int(i)
#         count_prime = 0

#         for k in range(1, num + 1):
#             if num % k == 0:   # ✅ FIXED HERE
#                 count_prime += 1

#         if count_prime == 2:  # ✅ Prime check
#             count += 1

# print("Prime digits count:", count)


# st = input("Enter a numeric string: ")
# prime = "2357"
# count = 0

# for ch in st:
#     if ch in prime:
#         count += 1

# print("Prime digits count:", count)

#===========================================================================

# 10. Sum of Digits in Alphanumeric String 3 Marks)
# Add only the digits from the input string Example: "a1b4c2" → 

# st = input("Enter the string :- ")

# sum = 0
# for ch in st:
#     if ch.isdigit():
#         sum = sum + int(ch)
# print("The sum is :- ",sum)

#===========================================================================

# 11. Leap Year Checker (3 Marks)
# Check if a given year is a leap year using correct logic

# year = int(input("Enter the year :- "))
# if year % 4 == 0 and year % 400 == 0 and year % 100 != 0:
#     print(year, "is a leap year")
# else:
#     print(year, "is not leap year")

#===========================================================================

# 2. Print Prime Numbers (2 to 100) (3 Marks)
# Print all prime numbers between 2 and 100 using loops


# for i in range(2 ,101):
    # count = 0
    # for j in range(1,i+1):
    #     if i%j==0:
    #         count+=1
    # if count == 2:
    #     print(j)

#===========================================================================

# 13. Factorial Using Loop 3 Marks)
# Take a number input and print its factorial using a for loop (no recursion)

# n = int(input("Enter the number :- "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print("The factorial is :- ",fact) 

#===========================================================================

# 14. Fibonacci Series Using Loop 3 Marks)
# Take n input, then print the first n Fibonacci numbers using loops only .
# Example for n=7 → 0 1 1 2 3 5 8

# n = int(input("Enter the number :- "))
# a=0
# b=1
# print("Fabonacci series :- ")
# print(a, end=" ")
# for i in  range(n+1):
#     a,b = a+b,a
#     print(a, end=" ")

#===========================================================================

# 15. Number Classification (3 Marks) 
# Take a number and prin t how many digits are:
# * Even digits # * Odd digits 
# * Zero digits*(Example: input: 302014 → even=2 odd=2 zero=2)

# n = int(input("Enter a number :- "))
# even = 0
# odd = 0
# zero = 0

# while n > 0:
#     d = n % 10

#     if d == 0:
#         zero += 1
#     elif d % 2 == 0:
#         even += 1
#     else:
#         odd += 1

#     n = n // 10   # remove last digit

# print("The even digits are :-", even)
# print("The odd digits are :-", odd)
# print("The zero digits are :-", zero)

