# 1. Hollow Pyramid Pattern
# Write a program to print a hollow pyramid using *. Use only for loops. Example (n = 5)

n =  5
for i in range(1,n+1):

    for j in range(n,0,-1):
        if j == i or i == n:
            print("* ", end=" ")
        else:
            print("  ", end=" ")


    for j in range(2,n+1):
        if j == i or i == n:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print('\n')

# 2. Rotate an Array
# Given a list of integers, rotate the list to the right by k positions.
# Example:
# Input:[1, 2, 3, 4, 5],k=2 Output: [4, 5, 1, 2, 3]


li = [1,2,3,4,5]

k = 2

left = 0
right = len(li)-1

while left < right:
    li[left],li[right] = li[right],li[left]
    left += 1
    right -= 1

left = 0
right = k-1

while left < right:
    li[left],li[right] = li[right],li[left]
    left += 1
    right -= 1


left = k
right = len(li)-1

while left < right:
    li[left],li[right] = li[right],li[left]
    left += 1
    right -= 1
print(li)


# 3. Reverse a String Without Using Built-in Functions
# Write a program to reverse a given string using a for loop.

st = input("Enter the string :- ")
rev = ""
for i in st:
    rev = i + rev
print(rev)

# 4. Count Vowels in a String
# Write a program to count the number of vowels in a given string.

st = input("Enter the string :- ")
vowel = "AEOIUaeiou"
count = 0
for i in st:
    if i in vowel:
        count += 1
print(count)


# 5. Find the Second Largest Element in a List
# Write a program to find the second largest element in a list without using sort().

li = [1,2,3,4,5]
sec = 0
max_ele = 0
for i in range(len(li)):
    sec = max_ele
    if max_ele < li[i]:
        max_ele = li[i]
print("The largest value is :- ",max_ele)
print("The second largest value is :- ",sec)


# 6. Check Palindrome (String)
# Write a program to check whether a given string is a palindrome or not.

st = input("Enter the string :- ")
rev = ""
for i in st:
    rev = i + rev
if rev == st:
    print("Plaindrome.....")
else:
    print("Not plaindrome....")

# 7. Remove Duplicate Elements from a List
# Write a program to remove duplicate elements from a list while maintaining the original
# order.

li = [1,6,2,2,3,4,5,5,5,5,6]

for i in range(len(li)):
    for j in range(len(li)-1, i, -1):
        if li[i] == li[j]:
            a = li.pop(j)
            print(a, "is removed....")

print("The list after removing duplicate elements is :-\n",li)


# 8. Sum of Even and Odd Numbers in a List
# Given a list of integers, write a program to calculate:
# ● sum of even numbers
# ● sum of odd numbers

li = [1,6,2,2,3,4,5,5,5,5,6]
odd_sum = 0
even_sum = 0
for i in range(len(li)):
    if li[i] % 2 == 0:
        even_sum += li[i]
    else:
        odd_sum += li[i]
print("Even element sum is :- ",even_sum)
print("Odd element sum is :- ",odd_sum)

# 9. Frequency of Each Character in a String
# Write a program to find the frequency of each character in a given string.
# Example:
# Input: "python"
# Output: p:1, y:1, t:1, h:1, o:1, n:1

st = "ppythonn"

for i in range(len(st)):
    count = 0
    repeated = False

    for k in range(i):
        if st[i] == st[k]:
            repeated = True

    if not repeated:
        for j in st:
            if st[i] == j:
                count += 1
        print(st[i], ":", count)

# 10. Move All Zeros to the End of the List
# Write a program to move all zeros in a list to the end without changing the order of non-zero elements.
# Example:
# Input: [1, 0, 3, 0, 5] Output: [1, 3, 5, 0, 0]

li = [0,0,0,1, 0, 3, 5] 
cpy = []
count = 0
for i in range(len(li)):
    if li[i] != 0:
        cpy.append(li[i])
    else:
        count += 1 
for i in range(count):
    cpy.append(0)
print(cpy)