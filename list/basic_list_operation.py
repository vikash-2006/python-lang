
                            #  LIST

# .append() --> add the element at the end of the list.
# .extend() --> add the multiple elements at the end of the list at once.
# .insert(index , element) --> is use to insert the element at the particular index.
# .pop(index) --> remove element by index but it default delete the element at the last of the list.
# .remove(elemet) --> remove element by giving to function directly. it does not return anything.
# .count(element) --> count method is use to the occurences or the frequency of the particular element is being passed to the count method
# .index(element) --> is use to find the index particular

# reverse the string

l1 = [1,2,3,4,5,6]
left = 0
right = len(l1)-1
while left <= right:
    l1[left],l1[right] = l1[right],l1[left]
    left+=1
    right-=1
print(l1)
# ===========================================================================

li = [1,2,3,4,5,6,7,8,9,10]

# first list  -> square of the elements -> odd index
# second list  -> cube of the elements -> even index

first_list=[]
second_list=[]

for i in range(len(li)):
    if i % 2 != 0:
        t = li[i]**2
        first_list.append(t)
    else:
        c = (li[i]**3)
        second_list.append(c)
print("First list :- ",first_list)
print("Second list :- ",second_list)
# ===========================================================================

# find the length of the list

li=[1,2,4,45,53,353,3,5,35]
count = 0
for i in li:
    count+=1
print(count)
# ===========================================================================

# FIND THE COMMAN ELEMENNT

l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]

for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            print(l1[i], end=" ")

for i in range(len(l1)):
    if l1[i] in l2:
        print(l1[i], end=" ")
# ===========================================================================

# check weather the list id plaindrome or not?

l1 = [1,2,9]
is_plaindorme = True
for i in range(len(l1)):
    if l1[i] != l1 [-(i+1)]:
        is_plaindorme = False
        break
if is_plaindorme:
    print("plaindorme")
else:
    print("not plaindorme")


l1 = ['aman','naman','ram']

for word in l1:
    if word == word[::-1]:
        print(word)

# ===========================================================================
# even number in --> even_list
# odd number in --> odd_list

li = [1,2,3,4,5,6,7,8,9,10]
even_list=[]
odd_list=[]
for num in li:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
print(odd_list)
print(even_list)

# ===========================================================================

# sum of list and list should be blanck.

    #   FIRST METHOD
li = [1,2,3,4,5,6,7,8]
sum = 0
while len(li) != 0:
    element = li.pop()
    sum += element
print("List is :- ",li)
print("Sum is :- ",sum)

    #   SECOND METHOD
for i in range(len(li)):
    i = 0
    sum+=li.pop()
print("List is :- ",li)
print("Sum is :- ",sum)

# ===========================================================================

li = [1,2,3,2,1,3,4,1,2]
a=li.count(1)
print(a)

# ===========================================================================

li = [1,2,3,4,5,6,7,8,9,10]
a=li.index(10)
print(a)

# ==========================================================================

li = [1,2,2,3,5,6,7,8,7,]
n = int(input("Enter the key :- "))
for i in range(len(li)):
    if n == li[i]:
        print(n,"is found at ",i)
        break

# ===========================================================================

# TARGET SUM

li = [1,2,3,4,5]
target = 7
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i] + li[j] == target:
            print(li[i], li[j])
        break

# ===========================================================================


# k time rotation
li = [1,2,3,4,5]
k = int(input("Enter the number :- "))

li = li[-k:] + li[:-k]

print(li)

# step 1 -> reversed the whole list
# step 2 -> reversed the list from k-1 index
# step 3 -> reverse the list from k to lenn(li)-1

li =  [1,2,3,4,5]

left = 0
right = len(li)-1
while left < right:
    li[left], li[right] = li[right], li[left]
    left += 1   
    right -= 1
print(li)
left = 0
right = k-1
while left < right:
    li[left], li[right] = li[right], li[left]
    left += 1
    right -= 1
print(li)
#   step 3
left = k
right = len(li)-1           
while left < right:
    li[left], li[right] = li[right], li[left]
    left += 1
    right -= 1
print(li)

# ===========================================================================

# product except self

# [1,2,3,4] -> [24,12,8,6]

li = [1,2,3,4]
l1=[]
for i in range(len(li)):
    k = li[i+1]* li[len(li)]
    l1.append(k)

pro  = 1
li = [1,2,3,4]
for num in li:
    pro *= num
for  i in range(len(li)):
    li[i] = (pro // li[i])
print(li)

# ===========================================================================

# remove duplicte elements form list

original_list = [1, 2, 3, 2, 4, 1, 5, 3]

new_list = []

for item in original_list:
    if item not in new_list:
        new_list.append(item)

print(new_list)


#==========================================================================\

# 2. Given a list, write code to display only the first and the last element.

li = [1,2,3,4,5]
print("First element of list :- ",li[0])
print("Last element of list :- ",li[-1])
#===========================================================================================

# 3. Determine and print the total number of elements in a list without utilizing the
# built-in len() function.

li = [1,2,3,4,5]
print("Total elements in list :- ",len(li))
#===========================================================================================

# 4. Modify a given list by adding a new element to its end, solely using list indexing
# and assignment (without using the append() method).

li = [1,2,3,4]
li = li + [None]
li[len(li)-1] = 5
print(li)
#===========================================================================================

# 5. In a pre-defined list, change the value of the element located at the third index
# position with a new specified value.

li = [1,2,3,4,5]
li[3] = 10
print(li)
#===========================================================================================

# 6. Develop a script that accepts 5 distinct inputs from the user and stores all of them
# sequentially in a single list.

li = []
for i in range(5):
    n = int(input(f"Enter the {i + 1} value :- "))
    li += [n]
print(li)
#===========================================================================================

# 7. Iterate through a given list using a for loop and print each element on a new line.

li = [1,2,3,4,5]
for i in range(len(li)):
    print(li[i])
#===========================================================================================

# 8. From a given list of integers, write code to print only the numbers that are even.

li = [1,2,3,4,5,6,7,8,9,10]
for n in li:
    if n % 2 == 0:
        print(n, end=" ")
#===========================================================================================

# 9. For a given list and a target number, calculate and print the total number of
# occurrences of the target number within the list.

li = [1,2,3,4,2,5,3,2,8,2]
key = int(input("Enter the number to find the occurence :- "))
count = 0
for i in li:
    if key == i:
        count += 1
    else:
        print("Not found in list.") 
print("The occurence of the given ", key, "number :- ",count)
#===========================================================================================

# 10. Calculate and print the sum of all numerical elements in a list without using the
# built-in sum() function.

li = [1,2,3,4,5]
sum = 0
for i in range(len(li)):
    sum += li[i]
print("The total sum is :- ",sum)