n=int(input("Enter the number :- "))
for i in range(n+1,1,-1):
    for j in range(1,n+1):
        if j<i:
            print(j ,end=" ")
        else:
            print(" ",end=" ")
    print("\n")