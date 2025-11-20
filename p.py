for i in range(1, 4 + 1):
    for j in range(1, 4 + 1):
        if j == 1 or i == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("\n")
