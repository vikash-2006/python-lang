# Write in files ->

# Here we are opening the file with name 'Detail.txt'
# 'w' -> write mode (permission)
# In write mode we basically grant the permission to write into the file.
# If the file doesn't exist, then it creates a new file.
# Otherwise, it overwrites the existing file.

file = open('Detail.txt', 'w')

# We have written something into the file.
# write function write the whole string into the file.
file.write('This is the details file.')

file.writelines(['\nMy name is John Doe.', '\nI am a software developer.'])
# writelines function writes a list of strings into the file.
# Each string from the list is written one after another.


# Since, when we open any file, then it goes into the RAM.
# It acquires some resources.
# When any operation has been performed on that file,
# then we should free the resource by closing that file.

file.close()
# Now, if we open the 'Detail.txt' file,




file = open('Detail.txt', 'a')
file.write('\nI love coding in Python.')
# 'a' -> append mode (permission)
# In append mode, we can add new data at the end of the file
file.close()
# Now, if we open the 'Detail.txt' file,
# we will see the new line added at the end of the file.
# if file doesn't exist, then it creates a new file.


file = open('Detail.txt', 'a+')

file.write('\nI also enjoy learning new technologies.')
# 'a+' -> append and read mode (permission)
# In append and read mode, we can add new data at the end of the file
# and also read the contents of the file.
file.close()
# Now, if we open the 'Detail.txt' file,
# we will see the new line added at the end of the file.


