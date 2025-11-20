a = int(input("Enter first numbe :- "))
b = int(input("Enter second number :- "))
c = int(input("Enter third number :- "))
lcm=0
if  a>b and a>c:
    lcm=a
elif b>c and b>a:
    lcm=b
elif c>a and c>b:
    lcm=c
else:
    lcm=a
while True:
    if lcm%a==0 and lcm%b==0 and lcm%c==0:
        print("LCM is : - ",lcm)
        break
    lcm+=1
