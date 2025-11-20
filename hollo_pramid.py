n = int(input("Enter the number :- "))
for i in range(1, n + 1):
    for j in range(n, 0, -1):
        if j == i or i == n:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    for k in range(2, n + 1):
        if k == i or i == n:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print("\n")
