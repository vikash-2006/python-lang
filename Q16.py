n = int(input("Enter the number :- "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j == i or j == 1 or i == n:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print("\n")