#   LCM FINDING BETWEEN TWO NUMBERS :----

a = int(input("Enter the number :- "))
b = int(input("Enter the number :- "))
lcm = 0
if a > b:
    lcm = a
else:
    lcm = b

while True:
    if lcm%a==0 and lcm%b==0:
        print("The lcm is :- ",lcm)
        break
    lcm+=1