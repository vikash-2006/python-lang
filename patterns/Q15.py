n = int(input("Enter the number :- "))
for i in range(1, n + 1):
    for j in range(1,n+1):
        if j == 1 or i == 1 or i == n or j == n:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print("\n")
        