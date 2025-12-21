n = int(input("Enter the number :- "))
count=0
if n==0:
    count=1
    print("The digits are :- ",count)
elif n<0:
    print("Invalid Input")
else:
    while n!=0:
        count+=1
        n=n//10
    print("The digits are :- ",count)