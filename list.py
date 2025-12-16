                # Basic List Questions 

# 1. Create a list of 5 arbitrary numerical values and print the list to the console.

# li = [1,2,3,4,5]
# print(li)

# 2. Given a list, write code to display only the first and the last element.

# li = [1,2,3,4,5]
# print("First element of list :- ",li[0])
# print("Last element of list :- ",li[-1])

# 3. Determine and print the total number of elements in a list without utilizing the
# built-in len() function.

# li = [1,2,3,4,5]
# print("Total elements in list :- ",len(li))

# 4. Modify a given list by adding a new element to its end, solely using list indexing
# and assignment (without using the append() method).

# li = [1,2,3,4]
# li = li + [None]
# li[len(li)-1] = 5
# print(li)

# 5. In a pre-defined list, change the value of the element located at the third index
# position with a new specified value.

# li = [1,2,3,4,5]
# li[3] = 10
# print(li)

# 6. Develop a script that accepts 5 distinct inputs from the user and stores all of them
# sequentially in a single list.

# li = []
# for i in range(5):
#     n = int(input(f"Enter the {i + 1} value :- "))
#     li += [n]
# print(li)

# 7. Iterate through a given list using a for loop and print each element on a new line.

# li = [1,2,3,4,5]
# for i in range(len(li)):
#     print(li[i])

# 8. From a given list of integers, write code to print only the numbers that are even.

# li = [1,2,3,4,5,6,7,8,9,10]
# for n in li:
#     if n % 2 == 0:
#         print(n, end=" ")

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

# 10. Calculate and print the sum of all numerical elements in a list without using the
# built-in sum() function.

# li = [1,2,3,4,5]
# sum = 0
# for i in range(len(li)):
#     sum += li[i]
# print("The total sum is :- ",sum)

                    # Intermediate List Questions


# 1. Identify and print the largest element present in a list of numbers without using the 
# built-in max() function.

# li = [1,2,3,4,6,4]
# max_ele = 0
# for i in range(len(li)):
#     if max_ele < li[i]:
#         max_ele = li[i]
# print("The highest element in list is :- ",max_ele)

# 2. Identify and print the smallest element present in a list of numbers without using the built-in 
# min() function.

# li = [1,2,3,0,4,5,6,7]
# min_ele = float('inf')

# for i in range(len(li)):
#     if li[i] < min_ele:
#         min_ele = li[i]
# print("The lowest element in list is :- ",min_ele)

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

