n=int(input("Enter the number :- "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(chr(64+j),end=" ")
        else:
            print(" ",end=" ")
    print("\n")