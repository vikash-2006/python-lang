# Set ==>> set is a datatype used to python to store the unqiue value
# set is unordered collection of element
# store unique values
#  

# Insilation of set
# the set can be insilation with the curly braces
# contain some elements into this

# s1 = {1,2,3,4}
# print(type(s1))
# ===================================================

# s2 = {}
# print(type(s2))
# ===================================================

# Empty set creation 
# use set() constructor

# s3 = set()
# print(type(s3))
# ===================================================

# store unique values

# s2 = {1,2,3,4,5,1,2,3}
# print(s2)

# ===================================================

# li=[1,2,3,4,1,2,3444,55,6]
# print(set(li))

# ===================================================
# Access the element

# li = {1,2,3,4,1,2,3444,55,6}
 
# for e in li:
#     print(e)
# ===================================================

# add new element

# li.add(7)
# print(li)
# li.add("Hello Vikash")
# print(li)
# ===================================================

# update is use t update or add multiple elements in existing set.

# li = {1,2,3,4,1,2,3444,55,6}
# li.update([1,2,3,10,"New","New2"])
# print(li)

# ===================================================

# l1 = [1,2,3,44,5,6,7]
# s2 = set(l1)
# print(s2)

# l2 = set()
# for i in range(5):
#     a = int(input("Enter the element :- "))
#     l2.add(a)
# print(l2)

# ele = set(map(int, input("Enter Elements :- ").split()))
# print(ele)

# ===================================================

# discard -->remove element  --> not found --> no error
# pop -->  remove element  --> randmoly

li = {1,2,3,4,1,2,3444,55,6}
li.remove(1)
print(li)


li.discard(1)
print(li)





