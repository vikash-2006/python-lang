# FABONACCI

n=int(input("Enter the number :- "))
print("FABONACCI SERIES :- ")
a=0
b=1

for i in range(n+1):
    a,b=a+b
    print(b ,end=' ')



