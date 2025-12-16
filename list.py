                # Basic List Questions 

# 1. Create a list of 5 arbitrary numerical values and print the list to the console.

# li = [1,2,3,4,5]
# print(li)
#===========================================================================================

# 2. Given a list, write code to display only the first and the last element.

# li = [1,2,3,4,5]
# print("First element of list :- ",li[0])
# print("Last element of list :- ",li[-1])
#===========================================================================================

# 3. Determine and print the total number of elements in a list without utilizing the
# built-in len() function.

# li = [1,2,3,4,5]
# print("Total elements in list :- ",len(li))
#===========================================================================================

# 4. Modify a given list by adding a new element to its end, solely using list indexing
# and assignment (without using the append() method).

# li = [1,2,3,4]
# li = li + [None]
# li[len(li)-1] = 5
# print(li)
#===========================================================================================

# 5. In a pre-defined list, change the value of the element located at the third index
# position with a new specified value.

# li = [1,2,3,4,5]
# li[3] = 10
# print(li)
#===========================================================================================

# 6. Develop a script that accepts 5 distinct inputs from the user and stores all of them
# sequentially in a single list.

# li = []
# for i in range(5):
#     n = int(input(f"Enter the {i + 1} value :- "))
#     li += [n]
# print(li)
#===========================================================================================

# 7. Iterate through a given list using a for loop and print each element on a new line.

# li = [1,2,3,4,5]
# for i in range(len(li)):
#     print(li[i])
#===========================================================================================

# 8. From a given list of integers, write code to print only the numbers that are even.

# li = [1,2,3,4,5,6,7,8,9,10]
# for n in li:
#     if n % 2 == 0:
#         print(n, end=" ")
#===========================================================================================

# 9. For a given list and a target number, calculate and print the total number of
# occurrences of the target number within the list.

# li = [1,2,3,4,2,5,3,2,8,2]
# key = int(input("Enter the number to find the occurence :- "))
# count = 0
# for i in li:
#     if key == i:
#         count += 1
#      else:
#         print("Not found in list.") 
# print("The occurence of the given ", key, "number :- ",count)
#===========================================================================================

# 10. Calculate and print the sum of all numerical elements in a list without using the
# built-in sum() function.

# li = [1,2,3,4,5]
# sum = 0
# for i in range(len(li)):
#     sum += li[i]
# print("The total sum is :- ",sum)
#===========================================================================================
#===========================================================================================
#===========================================================================================

                    # Intermediate List Questions


# 1. Identify and print the largest element present in a list of numbers without using the 
# built-in max() function.

# li = [1,2,3,4,6,4]
# max_ele = 0
# for i in range(len(li)):
#     if max_ele < li[i]:
#         max_ele = li[i]
# print("The highest element in list is :- ",max_ele)
#===========================================================================================

# 2. Identify and print the smallest element present in a list of numbers without using the built-in 
# min() function.

# li = [1,2,3,0,4,5,6,7]
# min_ele = float('inf')

# for i in range(len(li)):
#     if li[i] < min_ele:
#         min_ele = li[i]
# print("The lowest element in list is :- ",min_ele)
#===========================================================================================

# 3. Create a new list that contains the elements of the original list in reverse order,
#  without using the reverse() method or list slicing.

# li = [1,2,3,4,5]

# left = 0
# right = len(li)-1
# while left <= right:
#     li[left],li[right] = li[right],li[left]
#     left += 1
#     right -= 1
# print(li)
#===========================================================================================

# 4. Sort a list of numbers in ascending order using the logic of the 
# Bubble Sort algorithm, without using the built-in sort() method.

# nums = [64, 34, 25, 12, 22, 11, 90]

# n = len(nums)

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]

# print(nums)
#===========================================================================================

# 5. Generate a new list from an original list, where all duplicate 
# elements have been removed, without using the built-in set() function.

# original_list = [1, 2, 3, 2, 4, 1, 5, 3]

# new_list = []

# for item in original_list:
#     if item not in new_list:
#         new_list.append(item)

# print(new_list)
#===========================================================================================

# 6. Write a boolean function that checks whether a specified 
# element is contained within a given list.

# def contains_element(lst, element):
#     for i in lst:
#         if i == element:
#             return True
    # return False
#===========================================================================================

# 7. Print only the elements from a list that are 
# located at an index position which is an even number 0, 2, 4, ...)

# lst = [10, 20, 30, 40, 50, 60]

# for i in range(0, len(lst), 2):
#     print(lst[i])
#===========================================================================================

# 8. Print only the elements from a list that are located 
# at an index position which is an odd number 1, 3, 5, ...).

# lst = [10, 20, 30, 40, 50, 60]

# for i in range(1, len(lst), 2):
#     print(lst[i])
#===========================================================================================

# 9. Iterate through a list of integers and separately count 
# and print the total number of even numbers and the total number of odd numbers.

# numbers = [10, 21, 32, 43, 54, 65]

# even_count = 0
# odd_count = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Even numbers:", even_count)
# print("Odd numbers:", odd_count)
#===========================================================================================

# 10. Given a list of numbers, create and print a second list where 
# each element is the square of the corresponding element in the original list.

# numbers = [1, 2, 3, 4, 5]

# squared_list = []

# for num in numbers:
#     squared_list.append(num * num)

# print(squared_list)
#===========================================================================================

# 11. Combine the elements of two separate lists into a 
# single new list without using the + or extend() operators

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# new_list = []

# for item in list1:
#     new_list.append(item)

# for item in list2:
#     new_list.append(item)

# print(new_list)
#===========================================================================================

# 12. Modify a list in place so that all numbers less than zero (negative numbers) are removed.

# numbers = [10, -5, 20, -3, 0, -1, 15]

# i = 0
# while i < len(numbers):
#     if numbers[i] < 0:
#         numbers.pop(i)
#     else:
#         i += 1

# print(numbers)
#===========================================================================================

# 13. Determine and print the second largest numerical value
#  in a list without applying any sorting techniques.

# numbers = [10, 45, 23, 67, 89, 34]

# largest = second_largest = float('-inf')

# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num

# print("Second largest number:", second_largest)
#===========================================================================================

# 14. Implement a cyclic shift operation on a list where every element
#  is moved one position to the right, and the last element wraps 
#  around to the first position.

# numbers = [1, 2, 3, 4, 5]

# last = numbers[-1]

# for i in range(len(numbers) - 1, 0, -1):
#     numbers[i] = numbers[i - 1]

# numbers[0] = last

# print(numbers)
#===========================================================================================

# 15. Write a function that returns True if a list is currently
#  arranged in ascending order, and False otherwise.

# def is_ascending(lst):
#     for i in range(len(lst) - 1):
#         if lst[i] > lst[i + 1]:
#             return False
#     return True
#===========================================================================================
