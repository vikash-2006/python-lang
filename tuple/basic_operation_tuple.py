#==========================================================================
#==========================================================================
#========================================================================== 

                            # TUPLE

# Ordered collection of  elements 
# tuples are immutable
# once you created it cant be change after the creation
# can store duplicate elements
# defined by ()
# t1 = (1,2,3,4,5)
# it should have one element and one comma...


t = (1,2,3,4) 
print(type(t))
#==========================================================================

t1=()
print(type(t1))
#==========================================================================

t2 = (5,)
print(type(t2))

print(t[0])
#==========================================================================
    
# var = 1,2,3
# its treat as a tupple ==> is the  process 
# of grouping of multiple elements its automatically treat tuple ==>> it is know as tuple packing
# print(type(var))

t = ([1,2],[3,4])
t[0][1] =  100
print(t)
#==========================================================================

# here the whole list is changed not the tuple. here the whole list is cosidered as one element


# Tuple unpacking is a powerful Python feature that allows you to extract values from a tuple (or any iterable) and 
# assign them to multiple variables in a single, readable line of code.
# 
#========================================================================== 

t=(1,2,3,4,5,6,7,8)
sum = 0
for i in range(len(t)):
    sum+=t[i]
print("The sum is :- ",sum)
#==========================================================================

n =''
t1 = ('r','a','h','u','l')
for ch in t1:
    n = n + ch
print(n)
#==========================================================================

t = (1,2,3,4,5)
t[2] = 10
print(t)
# it will give error because tuple is immutable

#==========================================================================
t = (1,2,3,4,5)
t.append(6)
print(t)
# it will give error because tuple is immutable

#==========================================================================

t = (1,2,3,4,5)
print(len(t))

#==========================================================================

t = (1,2,3,4,5,1,2,3)
print(t.count(3))

#==========================================================================

t = (1,2,3,4,5,1,2,3)
print(t.index(3))

#==========================================================================

t = (1,2,3,4,5)
for i in t:
    print(i)

#==========================================================================

t = (1,2,3,4,5)
for i in range(len(t)):
    print(t[i])
    
#==========================================================================



