"""
========================================================
PYTHON DICTIONARY PRACTICE PROGRAMS
========================================================
"""

# -------------------------------------------------------
# Q1. Create a dictionary and access value using key
# -------------------------------------------------------
d = {
    'first': 1,
    'second': 2,
    'third': 3
}

# Access value using key
print(d['first'])


# -------------------------------------------------------
# Q2. Create and print a student dictionary
# Keys are immutable, values are mutable
# -------------------------------------------------------
student = {
    'Name': 'Vikash',
    'Class': 'A23',
    'Surname': 'Kumawat'
}

print(student)


# -------------------------------------------------------
# Q3. Create dictionary using dict() constructor
# -------------------------------------------------------
d2 = dict(name='Vikash', rollno=25, batch='A23')
print(d2)


# -------------------------------------------------------
# Q4. Dictionary with list as values
# -------------------------------------------------------
data = {
    'Name': ['ram', 'shyam', 'naman'],
    'rollno': [23, 45, 67]
}

print(data)


# -------------------------------------------------------
# Q5. Access value using get() method
# get() does not give error if key is missing
# -------------------------------------------------------
print(student.get('Name', 'Not present'))


# -------------------------------------------------------
# Q6. Iterate dictionary and print key-value pairs
# -------------------------------------------------------
for key in student:
    print(f'{key} --> {student[key]}')


# -------------------------------------------------------
# Q7. Print all keys of a dictionary
# -------------------------------------------------------
print(student.keys())


# -------------------------------------------------------
# Q8. Update values in dictionary
# -------------------------------------------------------
person = {
    'Name': 'Rahul',
    'Age': 18,
    'GF': 'Monu'
}

person['Name'] = 'Guddu'
person['Age'] = 16
person['GF'] = 'Radha'

print(person)


# -------------------------------------------------------
# Q9. Find sum of all values in dictionary
# -------------------------------------------------------
d3 = {'a': 1, 'b': 2, 'c': 3}

total = 0
for key in d3:
    total += d3[key]

print("Sum =", total)


# -------------------------------------------------------
# Q10. Find maximum and minimum value in dictionary
# -------------------------------------------------------
d4 = {'a': 1, 'b': 2, 'c': 3}

max_val = 0
for key in d4:
    if max_val < d4[key]:
        max_val = d4[key]

min_val = max_val
for key in d4:
    if min_val > d4[key]:
        min_val = d4[key]

print("Max =", max_val)
print("Min =", min_val)


# -------------------------------------------------------
# Q11. Print dictionary values greater than 50
# -------------------------------------------------------
d5 = {'a': 10, 'b': 200, 'c': 60}

for key in d5:
    if d5[key] > 50:
        print(f'{key} -> {d5[key]}')


# -------------------------------------------------------
# Q12. Swap keys and values of a dictionary
# -------------------------------------------------------
swapped = {}

for key, value in student.items():
    swapped[value] = key

print(swapped)


# -------------------------------------------------------
# Q13. Add new keys to dictionary
# -------------------------------------------------------
student_data = {'Name': 'Vikash'}

student_data['Address'] = 'Jaipur'
student_data.update({'Roll': 11})

print(student_data)


# -------------------------------------------------------
# Q14. Create dictionary using two lists
# -------------------------------------------------------
keys = ['Name', 'Batch', 'Rollno']
values = ['Rohan', 'A23', 35]

result = {}
for i in range(len(keys)):
    result[keys[i]] = values[i]

print(result)


# -------------------------------------------------------
# Q15. Count frequency of elements (using get method)
# -------------------------------------------------------
string = 'a b b c c d a e'
items = string.split()

freq = {}
for ch in items:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)


# -------------------------------------------------------
# Q16. Print only repeated elements and their count
# -------------------------------------------------------
for key in freq:
    if freq[key] > 1:
        print(key, ":", freq[key])


# -------------------------------------------------------
# Q17. Merge two dictionaries
# -------------------------------------------------------
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'e': 5, 'f': 6}

d1.update(d2)
print(d1)


# -------------------------------------------------------
# Q18. Square all values of dictionary
# -------------------------------------------------------
d_square = {'a': 1, 'b': 4, 'c': 3}

for key in d_square:
    d_square[key] = d_square[key] ** 2

print(d_square)


# -------------------------------------------------------
# Q19. Count number of keys in dictionary
# -------------------------------------------------------
count = 0
for key in d_square:
    count += 1

print("Total keys =", count)


# -------------------------------------------------------
# Q20. Find product of all values in dictionary
# -------------------------------------------------------
product = 1
for key in d_square:
    product *= d_square[key]

print("Product =", product)


# -------------------------------------------------------
# Q21. Find product of all values in dictionary
# -------------------------------------------------------
