n=int(input("Enter the number :- "))
for i in range(1,n+1):
    temp=1
    for j in range(n,0,-1):
        if j<i: 
            print(temp , end=" ")
            temp+=1
        else:
            print(" ", end=" ")
    temp -=2
    for k in range(2,n+1):
        if k<i:
            print(temp , end=" ")
            temp -=1
        else:
            print("  ", end=" ")
    print("\n")