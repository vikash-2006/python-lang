n = int(input("Enter the number :- "))
rev=0
temp=n
while n>0:
    d=n%10
    n=n//10
    rev=rev*10+d
if temp==rev:
    print("Given number is Plaindrome",rev)
else:
    print("Given number is not Plaindrome",rev)