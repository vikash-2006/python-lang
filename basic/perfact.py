n = int(input("Enter the number :- "))
temp=n
i=1
sum=0
while i<n:
    if n % i ==0:
       sum = sum+i
    i+=1
if temp == sum:
    print("Given number is perfact number :- ", sum)
else:
    print("Given number is not perfact number  :-  ", sum)