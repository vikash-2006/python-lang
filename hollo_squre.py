n = int(input("Enter the number :- "))
for i in range(n):
    for j in range(n):
        if i==0 or  j==0  or i==j :
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    for j in range(n):
        if i==0 or  j==0 or j==n-1 or j==i or j<=i:
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print("\n")  

for i in range(n):
    for j in range(n):
        if i==n-1 or j==0 or j==i:
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    for j in range(n):
        if i==n-1 or j==0 or j==n-1 or j==i:
            print("* ",end=" ")
        else:
            print("  ",end=" ")
    print("\n")