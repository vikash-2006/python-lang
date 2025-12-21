n=int(input("Enter the number :- "))
temp=1
for i in range(0,n):
    for j in range(0,n):
        if j<=i:
            print(temp ,end=" ")
            temp+=1
        else:
            print(" ",end=" ")
    print("\n")