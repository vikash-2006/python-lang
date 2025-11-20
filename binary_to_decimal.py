n = int(input("Enter any binary number :- "))

sum = 0
i=0
while n>0:
    last = n%10
    sum = sum+(2**i)*last
    i+=1
    n=n//10
print(sum) 
