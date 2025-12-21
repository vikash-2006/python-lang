n = int(input("Enter the number :- "))

for i in range(1, n + 1):
    # Left side
    for j in range(n, 0, -1):
        if j <= i:
            print("* ", end=" ")
        else:
            print("  ", end=" ")

    # Right side
    for j in range(2, n + 1):
        if j <= i:
            print("* ", end=" ")
        else:
            print("  ", end=" ")

    print("\n")